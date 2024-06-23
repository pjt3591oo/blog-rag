import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import time, random

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')

def main():
    page_log = 'page_log.log'
    index = 0
    with open(page_log, 'r') as f:
        lines = f.readlines()
        for line in lines:
            index += 1
            log_no = line.split(',')[0]
            url = f'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo={log_no}'
            loader = WebBaseLoader(url)

            docs = loader.load()

            print()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)

            delay = random.randrange(300, 700)
            
            # 임베딩 인덱싱
            vectorstore = Chroma.from_documents(
                persist_directory='chroma',
                documents=splits,
                embedding=OpenAIEmbeddings()
            )
            vectorstore.persist()

            print(f'[{index} / {len(lines)}] log no: {log_no}, docs length: {len(docs)}, text length: {len(splits)}, delay: {delay}ms')
            time.sleep(delay/1000)

if __name__ == "__main__":
    main()