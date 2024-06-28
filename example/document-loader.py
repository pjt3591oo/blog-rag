from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from bs4 import SoupStrainer
import re

def replace_multiple_newlines(text):
    # 2개 이상의 연속된 줄 바꿈 문자를 하나로 치환
    result = re.sub(r'\n+', '\n', text)
    return result

log_no = '223488345638'
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

for doc in docs:
    doc.page_content = replace_multiple_newlines(doc.page_content)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)


for split in splits:
    print(split.page_content)
    print()

print(len(splits))