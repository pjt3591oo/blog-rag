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

 [참고] 임베딩 정보(223488345638을 기준으로 1500개 embedding 후 실행겨과)

```sh
export OPENAI_API_KEY=

python3 example/vector-query.py
```

```
[Document(page_content='해석하면 master는 워커의 시그널을 받고 워커가 종료되면 다시 시작하도록 합니다. 공식문서를 확인하면 worker는 sync worker, async worker, tornado worker, asyncio worker로 나뉩니다.\u200b\u200b▶ 파이썬에서 비동기가 좋을까? 비동기는 언어를 동작하는 환경의 메커니즘이 굉장히 중요합니다. uvicorn에서 nodejs에서 사용하기 위해 만든 libuv를 사용하는 것만 봐도 알 수 있습니다. 또한 파이썬은 단순히 스크립트 언어로써 비동기를 제공하는 것이 쉽지만은 않습니다. 사실 nodejs와 python을 비교하는 경우를 종종 보긴했는데 nodejs는 프로그램이 동작하는 환경이며 프로그래밍 언어인 python은 javascript와 비교하는것이 좀 더 정확합니다. 자바스크립트 또한 V8에서 구동하는데 비동기를 위해 libuv를 만든것이거든요. 단순히 스키립트로써 발전해온 파이썬은 기존의 많은 라이브러리/프레임워크들은 비동기를 고려되지 않고 설계되었습니다. \u200b 그렇기 때문에 디비 라이브러리 중 SQLAlchemy가 있는데 asyncpg라는 것을 통해 어댑터에 등록해줘야 비동기 형태로 사용가능했습니다. 다행스럽게도 1.4 버전부터는 connection pool을 이용한다면 어댑터를 사용하지 않더라도 비동기 형태로 사용가능합니다.\u200b 프레임워크가 비동기 형태로 제공하더라도 라이브러리가 비동기 형태로 제공하지 않는다면 비동기 프레임워크를 쓰는게 큰 의미가 없습니다. 이 부분이 javascript를 동작하는 nodejs 환경과 가장 큰 차이점을 가지고 있습니다. javascript는 애초에 비동기 환경인 브라우저 또는 nodejs 환경에서 동작하다 보니 모든 라이브러리가 비동기적인 특성이 고려되서 개발되었습니다. 물론 비동기를 처리하는 방식이 달라지긴 했지만 결과론적으론 비동기를 다룰 수 있는 형태가 상당히 많습니다.\u200b사실 파이썬에서 비동기적인 구조를 가져가는게 파이썬을 잘 사용하는 건지는 아직은 잘 모르겠습니다. 그래도 노드를', metadata={'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222772705407', 'title': '[fastapi] uvicorn, fastapi 비동기 메커니즘 이해 : 네이버 블로그'}), Document(page_content='dart도 Javascript처럼 비동기를 제공합니다. 하필 Javascript처럼 이라고 표현한 이유는 Javascript에서 처리하는 비동기 처리방식과 매우 유사한 방식을 사용하기 때문입니다.\u200b제목에서도 알 수 있듯이 async, await, future를 사용하는데 future는 Javascript의 Promise와 매우매우매우 유사합니다.\u200b만약, Javascript에서 Promise, async/await 사용법을 자유자재로 구사할 줄 안다면 해당글을 매우 쉽게 읽을 수 있습니다.\u200b※ 비동기란? 비동기가 무엇인지 간단하게 설명을 하면 기다리지 않고 다음 코드를 실행하세요 입니다.\u200b 서버로부터 데이터를 받아온 후 출력해준다고 가정해보겠습니다. A 프로그램에서 서버로 데이터를 데이터 요청을 합니다. 그런데 이 프로그램은 서버로 부터 응답을 언제 받는다고 예측이 불가능 합니다. 즉, 실행시간 예측을 할 수 없습니다. 여기서 기다리는 시간동안 뒤의 코드를 실행하고 실행 결과에 대한 처리코드를 별도로 등록하여 서버로부터 응답이 왔다면 등록해둔 처리코드를 실행합니다.\u200b 앞에서 기다리지 않는다는 의미가 어려울 수 있습니다. 쉽게 이해하기 위해 비동기로 동작하는 함수는 다른 녀석이 가져가서 실행한 후 결과를 현재 다트를 실행하는 놈에게 알려줍니다. 여기서 알려주는기 위해 전달하는 것이 실행 결과에 대한 처리코드로 보시면 됩니다. 이를 콜백함수라고 합니다. 해당 작업을 완료하면 콜백함수를 원래의 다트를 실행하는 놈이 실행할 수 있도록 합니다. \u200b이처럼 코드를 호출한 시점에서 코드가 실행되지 않고 추후에 실행되는 방법을 비동기라고 합니다. 여기서 핵심은 기다리지 않는다입니다.\u200bdart에선 이러한 비동기를 제공하기 위해 future를 이용하며 async/await를 함께 사용합니다.\u200b이렇게 복잡한 비동기를 배우는 이유는 적은 자원으로 고효율을 낼 수 있기 때문입니다. 하지만, 우리는 비동기간 코드가 실행시점을 명확히 알 수 없지만 이를 논리적으로 코드를 짜기 위해', metadata={'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222314109684', 'title': '[dart] Asynchronous(비동기) - async, await, future : 네이버 블로그'}), Document(page_content='[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기 : 네이버 블로그\n\n\n\n\n\n\n\n\n\n\n\n\nNAVER\n블로그\n\n\n\n\n멍개의 연구소\n\n\n\n\n\n블로그 검색\n\n\n이 블로그에서 검색\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n공감\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t첫 댓글을 남겨보세요\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\n\n\n\n\n\n\n\n\n\n공유하기\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n메뉴 바로가기\n본문 바로가기\n\n\n\n\n내 블로그 \n\n\n이웃블로그\n\n\n\n\n\n\n\n블로그 홈 \n\n로그인\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n블로그 메뉴\n\n\n\n\n\n프롤로그\n\n\n\n블로그\n\n\n\n\nServer\n\n\n\n\nClient\n\n\n\n프로그래밍 \n\n\n\n인공지능\n\n\n\n\n\n서재\n\n\n\n메모\n\n\n\n태그\n\n\n\n안부\n\n\n\n\n\n\n멍개의 연구소\n\n\n\n\n\n\n블로그\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n글쓰기\n\n\n\n\n가벼운 글쓰기툴 퀵에디터가 오픈했어요!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n공지 목록\n\n\n\n\n\n\n\n공지글\n\n\n\n\n\n\n글 제목\n작성일\n\n\n\n\n\n\n\n(6)\n\n\n공지\n굿즈 제작 & 판매\n\n\n\n\n2022. 9. 1.\n\n\n\n\n\n\n(25)\n\n\n공지\n티스토리 이관 공지\n\n\n\n\n2022. 8. 24.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n전체보기 2,919개의 글\r\n\t\t\t\t\t\t\n전체보기목록열기\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPython\n\n\n\n\n[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기  \n\n\n\n\n\n멍개\n\n ・ \n2020. 5. 26. 23:37\n\n\nURL 복사\n 이웃추가\n\n본문 기타 기능\n\n\n                   공유하기\n                \n\n신고하기', metadata={'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=221979921090', 'title': '[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기 : 네이버 블로그'}), Document(page_content='애초에 비동기 환경인 브라우저 또는 nodejs 환경에서 동작하다 보니 모든 라이브러리가 비동기적인 특성이 고려되서 개발되었습니다. 물론 비동기를 처리하는 방식이 달라지긴 했지만 결과론적으론 비동기를 다룰 수 있는 형태가 상당히 많습니다.\u200b사실 파이썬에서 비동기적인 구조를 가져가는게 파이썬을 잘 사용하는 건지는 아직은 잘 모르겠습니다. 그래도 노드를 메인으로 사용하는 저로써는 libuv를 파이썬에서 사용했다는 사실만으로도 참 기분이 좋아지네요 ㅎㅎ', metadata={'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222772705407', 'title': '[fastapi] uvicorn, fastapi 비동기 메커니즘 이해 : 네이버 블로그'})]
해석하면 master는 워커의 시그널을 받고 워커가 종료되면 다시 시작하도록 합니다. 공식문서를 확인하면 worker는 sync worker, async worker, tornado worker, asyncio worker로 나뉩니다.▶ 파이썬에서 비동기가 좋을까? 비동기는 언어를 동작하는 환경의 메커니즘이 굉장히 중요합니다. uvicorn에서 nodejs에서 사용하기 위해 만든 libuv를 사용하는 것만 봐도 알 수 있습니다. 또한 파이썬은 단순히 스크립트 언어로써 비동기를 제공하는 것이 쉽지만은 않습니다. 사실 nodejs와 python을 비교하는 경우를 종종 보긴했는데 nodejs는 프로그램이 동작하는 환경이며 프로그래밍 언어인 python은 javascript와 비교하는것이 좀 더 정확합니다. 자바스크립트 또한 V8에서 구동하는데 비동기를 위해 libuv를 만든것이거든요. 단순히 스키립트로써 발전해온 파이썬은 기존의 많은 라이브러리/프레임워크들은 비동기를 고려되지 않고 설계되었습니다.  그렇기 때문에 디비 라이브러리 중 SQLAlchemy가 있는데 asyncpg라는 것을 통해 어댑터에 등록해줘야 비동기 형태로 사용가능했습니다. 다행스럽게도 1.4 버전부터는 connection pool을 이용한다면 어댑터를 사용하지 않더라도 비동기 형태로 사용가능합니다. 프레임워크가 비동기 형태로 제공하더라도 라이브러리가 비동기 형태로 제공하지 않는다면 비동기 프레임워크를 쓰는게 큰 의미가 없습니다. 이 부분이 javascript를 동작하는 nodejs 환경과 가장 큰 차이점을 가지고 있습니다. javascript는 애초에 비동기 환경인 브라우저 또는 nodejs 환경에서 동작하다 보니 모든 라이브러리가 비동기적인 특성이 고려되서 개발되었습니다. 물론 비동기를 처리하는 방식이 달라지긴 했지만 결과론적으론 비동기를 다룰 수 있는 형태가 상당히 많습니다.사실 파이썬에서 비동기적인 구조를 가져가는게 파이썬을 잘 사용하는 건지는 아직은 잘 모르겠습니다. 그래도 노드를
{'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222772705407', 'title': '[fastapi] uvicorn, fastapi 비동기 메커니즘 이해 : 네이버 블로그'}

========
dart도 Javascript처럼 비동기를 제공합니다. 하필 Javascript처럼 이라고 표현한 이유는 Javascript에서 처리하는 비동기 처리방식과 매우 유사한 방식을 사용하기 때문입니다.제목에서도 알 수 있듯이 async, await, future를 사용하는데 future는 Javascript의 Promise와 매우매우매우 유사합니다.만약, Javascript에서 Promise, async/await 사용법을 자유자재로 구사할 줄 안다면 해당글을 매우 쉽게 읽을 수 있습니다.※ 비동기란? 비동기가 무엇인지 간단하게 설명을 하면 기다리지 않고 다음 코드를 실행하세요 입니다. 서버로부터 데이터를 받아온 후 출력해준다고 가정해보겠습니다. A 프로그램에서 서버로 데이터를 데이터 요청을 합니다. 그런데 이 프로그램은 서버로 부터 응답을 언제 받는다고 예측이 불가능 합니다. 즉, 실행시간 예측을 할 수 없습니다. 여기서 기다리는 시간동안 뒤의 코드를 실행하고 실행 결과에 대한 처리코드를 별도로 등록하여 서버로부터 응답이 왔다면 등록해둔 처리코드를 실행합니다. 앞에서 기다리지 않는다는 의미가 어려울 수 있습니다. 쉽게 이해하기 위해 비동기로 동작하는 함수는 다른 녀석이 가져가서 실행한 후 결과를 현재 다트를 실행하는 놈에게 알려줍니다. 여기서 알려주는기 위해 전달하는 것이 실행 결과에 대한 처리코드로 보시면 됩니다. 이를 콜백함수라고 합니다. 해당 작업을 완료하면 콜백함수를 원래의 다트를 실행하는 놈이 실행할 수 있도록 합니다. 이처럼 코드를 호출한 시점에서 코드가 실행되지 않고 추후에 실행되는 방법을 비동기라고 합니다. 여기서 핵심은 기다리지 않는다입니다.dart에선 이러한 비동기를 제공하기 위해 future를 이용하며 async/await를 함께 사용합니다.이렇게 복잡한 비동기를 배우는 이유는 적은 자원으로 고효율을 낼 수 있기 때문입니다. 하지만, 우리는 비동기간 코드가 실행시점을 명확히 알 수 없지만 이를 논리적으로 코드를 짜기 위해
{'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222314109684', 'title': '[dart] Asynchronous(비동기) - async, await, future : 네이버 블로그'}

========
[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기 : 네이버 블로그


Python


[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기

멍개

 ・
2020. 5. 26. 23:37


신고하기
{'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=221979921090', 'title': '[python] asyncio를 이용한 비동기 처리 이해와 promise와 비교하기 : 네이버 블로그'}

========
애초에 비동기 환경인 브라우저 또는 nodejs 환경에서 동작하다 보니 모든 라이브러리가 비동기적인 특성이 고려되서 개발되었습니다. 물론 비동기를 처리하는 방식이 달라지긴 했지만 결과론적으론 비동기를 다룰 수 있는 형태가 상당히 많습니다.사실 파이썬에서 비동기적인 구조를 가져가는게 파이썬을 잘 사용하는 건지는 아직은 잘 모르겠습니다. 그래도 노드를 메인으로 사용하는 저로써는 libuv를 파이썬에서 사용했다는 사실만으로도 참 기분이 좋아지네요 ㅎㅎ
{'language': 'ko', 'source': 'https://blog.naver.com/PostView.naver?blogId=pjt3591oo&logNo=222772705407', 'title': '[fastapi] uvicorn, fastapi 비동기 메커니즘 이해 : 네이버 블로그'}

========
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

[참고] 임베딩 정보(223488345638을 기준으로 1500개 embedding 후 실행결과)

```
Python의 비동기 모델은 asyncio를 사용하여 구현됩니다. asyncio는 이벤트 루프를 기반으로 한 비동기 프로그래밍을 지원하는 라이브러리로, async/await 구문을 사용하여 비동기 코드를 작성할 수 있습니다. 이를 통해 여러 작업을 동시에 처리하고, I/O 바운드 작업을 효율적으로 처리할 수 있습니다. asyncio를 이용하면 비동기적인 작업을 처리하고 결과를 기다리지 않고 다음 작업을 실행할 수 있습니다.
```