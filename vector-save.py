import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')


url = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EC%A0%95%EC%B1%85%EA%B3%BC_%EC%A7%80%EC%B9%A8'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print(len(splits))

# 인덱싱
vectorstore = Chroma.from_documents(
    persist_directory='chroma',
    documents=splits,
    embedding=OpenAIEmbeddings()
)
vectorstore.persist()
