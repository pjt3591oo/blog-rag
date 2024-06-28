import os, time, random, re
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from bs4 import SoupStrainer

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')

def replace_multiple_newlines(text):
    # 2개 이상의 연속된 줄 바꿈 문자를 하나로 치환
    result = re.sub(r'\n+', '\n', text)
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
                doc.page_content = replace_multiple_newlines(doc.page_content)

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