import os, time, random, re
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from bs4 import SoupStrainer

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')

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

    result = re.sub(r'\xa0', '', result)
    result = re.sub(r'\u200b', '', result)

    return result

def main():
    page_log = 'page_log.log'
    index = 0
    
    with open(page_log, 'r') as f:
        lines = f.readlines()
        for line in lines:
            index += 1
            log_no = line.split(',')[0]
            url = f'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo={log_no}'
            loader = WebBaseLoader(
                    web_path=url,
                    bs_kwargs=dict(
                        parse_only=SoupStrainer(
                            "div", 
                            attrs={
                                "class": [
                                    "pcol1", "se-main-container" # 제목, 본문
                                ]
                            }
                        )
                    )
            )

            docs = loader.load()
            # 2개 이상의 연속된 줄 바꿈 문자를 하나로 치환
            for doc in docs:
                doc.page_content = replace_no_need(doc.page_content)

            print()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)

            # 임베딩 인덱싱
            vectorstore = Chroma.from_documents(
                persist_directory='chroma',
                documents=splits,
                embedding=OpenAIEmbeddings()
            )
            vectorstore.persist()

            delay = random.randrange(300, 700)
            print(f'[{index} / {len(lines)}] log no: {log_no}, docs length: {len(docs)}, text length: {len(splits)}, delay: {delay}ms')
            time.sleep(delay/1000)

if __name__ == "__main__":
    main()