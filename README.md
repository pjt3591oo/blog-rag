# blog기반 RAG

### example

* llm prompt

```sh
export OPENAI_API_KEY=

python3 example/llm-basic.py
```

* vectordb save

```sh
export OPENAI_API_KEY=

python3 example/vector-save.py
```

* vectordb query

```sh
export OPENAI_API_KEY=

python3 example/vector-query.py
```

### usage

* 포스팅 아이디 수집

```sh
export OPENAI_API_KEY=

python3 blog-save-post-id.py
```

블로그 포스트의 id를 page_log.log로 쌓는다.

* 포스팅 정보 임베딩

페이지 목록인 page_log.log에서 페이지 아이디를 이용하여 페이지 정보를 가져온 후 chroma 디비에 저장

```sh
export OPENAI_API_KEY=
export BLOG_ID=pjt3591oo

python3 blog-post-embedding.py
```

* rag.py 실행

```sh
export OPENAI_API_KEY=

python3 rag.py
```

