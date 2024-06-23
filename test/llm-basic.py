import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

if (not os.environ['OPENAI_API_KEY']):
    raise Exception('OPENAI_API_KEY is not set')

# model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# chain 실행
rst0 = llm.invoke("지구의 자전 주기는?")
print(rst0)

prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. : {input}")
chain = prompt | llm
rst1 = chain.invoke({"input": "지구의 자전 주기는?"})

print(rst1)