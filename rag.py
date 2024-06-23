import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')


# Prompt
template = '''Answer the question based only on the following context:
{context}

Question: {question}
'''

prompt = ChatPromptTemplate.from_template(template)

# LLM
model = ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0)

# vectorDB 
vectorstore = Chroma(
    persist_directory='chroma',
    embedding_function=OpenAIEmbeddings()
)

# Rretriever
retriever = vectorstore.as_retriever()

# Combine Documents
def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

# RAG Chain 연결
rag_chain = (
    {'context': retriever | format_docs, 'question': RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# Chain 실행
question = "python의 비동기 모델을 설명해줘"
answer = rag_chain.invoke(question)

print(f"Question: {question}")
print(f"Answer: {answer}")