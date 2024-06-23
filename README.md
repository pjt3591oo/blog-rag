# blog기반 RAG

### 환경변수 설정

```sh
export OPENAI_API_KEY=
```

### 임베딩 정보

[solidity] solidity storage layout 이해하기 ~ [ethereum] geth 테스트중 까지 임베딩 완료

포스트 갯수: 1151

### flow

1. blog-save-post-id.py 실행

블로그 포스트의 id를 page_log.log로 쌓는다.

2. blog-post-embedding.py 실행

페이지 목록인 page_log.log에서 페이지 아이디를 이용하여 페이지 정보를 가져온 후 chroma 디비에 저장

3. rag.py 실행

rag 실행