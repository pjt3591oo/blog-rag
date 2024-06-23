import os
import requests as rq
import json 
import time
from urllib import parse

if (not os.environ['BLOG_ID']):
    raise Exception('BLOG_ID is not set')


def main():
    page = 0
    blog_id = os.environ['BLOG_ID']
    page_log = 'page_log.log'
    current_page_log_no = 30
    page_log_file = open(page_log, 'w')

    while True:
        page += 1

        pagination_url = f'https://blog.naver.com/PostTitleListAsync.naver?blogId={blog_id}&viewdate=&currentPage={page}&categoryNo=0&parentCategoryNo=&countPerPage={current_page_log_no}'
        res = rq.get(pagination_url)
        
        print(f'>>>>>>>>>>>>>> page: {page} search... <<<<<<<<<<<<<<<<')

        if res.status_code != 200:
            print('Failed to fetch data')
            return
        
        data = json.loads(res.text.replace('\\', '\\\\'))

        if data['resultCode'] == 'E':
            print(data['resultMessage'])
            break

        if len(data['postList']) < current_page_log_no:
            print('No more data')
            break
        
        for post in data['postList']:
            print(post['logNo'], parse.unquote(post["title"]), post["categoryNo"], post["parentCategoryNo"])
            page_log_file.write(f'{post["logNo"]}, {parse.unquote(post["title"])}, {post["categoryNo"]}, {post["parentCategoryNo"]}\n')

        time.sleep(1)

if __name__ == "__main__":
    main()