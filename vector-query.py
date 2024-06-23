import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')

# vectorstore 디비 커넥션
vectorstore = Chroma(
    persist_directory='chroma',
    embedding_function=OpenAIEmbeddings()
)

docs = vectorstore.similarity_search(
    "python의 비동기 모델을 설명해줘"
)
for doc in docs:
    print(doc.page_content.replace('\n\n\n', '\n'))
    print(doc.metadata)
    print()
    print('========')