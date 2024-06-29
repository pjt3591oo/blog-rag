from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from bs4 import SoupStrainer
import re

def recursive_replace(text):
    before = len(text)

    result = re.sub(r'\n\t', '\n', text)
    result = re.sub(r'\n+', '\n', result)
    result = re.sub(r'\t+', '\t', result)

    after = len(result)

    if before != after:
        return recursive_replace(result)

    return result

def replace_no_need(text):
    pattern = r'\d{4}\.\s*\d{1,2}\.\s*\d{1,2}\.\s*\d{1,2}:\d{1,2}\s'
    result = re.sub(pattern, '\n', text)

    result = recursive_replace(result)

    t='''\n멍개\n ・ \nURL 복사\n 이웃추가\n본문 기타 기능\n                   공유하기\n                \n신고하기\n'''
    result = result.replace(t, ' ')

    return result


log_no = '100178851757'
url = f'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo={log_no}'

loader = WebBaseLoader(
    web_path=url,
    bs_kwargs=dict(
        parse_only=SoupStrainer(
            "div", 
            attrs={
                "id": [f'post-view{log_no}', 'title_1' ]
            }
        )
    )
)

docs = loader.load()

for doc in docs:
    doc.page_content = replace_no_need(doc.page_content)
    # doc.page_content = doc.page_content.replace('URL 복사\n 이웃추가\n본문 기타 기능\n                   공유하기\n                \n신고하기\n', ' ')
    print(doc)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)



# for split in splits:
#     print(split.page_content)
#     print()

# print(len(splits))