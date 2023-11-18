## 설명

1. setting.py : 프로젝트를 진행하는데 여러가지 세팅
2. urls.py : 사용자의 경로를 누가 처리하는가를 설정(라우팅)
3. manage.py : 프로젝트를 진행하는데 사용하는 유틸리티 파일
    - python manage.py runserver : 서버 키기
    - ctrl + C : 명령어 취소
----
 - manage.py -> myproject_01.urls.py -> myapp.urls.py : api 주소에 따른 페이지 생성
 - view.py : pront 생성

----
- GET 과정 : get 하다
 - http://localhost:8000/read/1/ : 일반적인 페이지
 - http://localhost:8000/read/?id=1 : 쿼리 스트링형식, 서버의 데이터를 변경하는 과정인데 이렇게되면 데이터가 유출이됨 이러면 절대안된다.
 - 위 URL의 공통점: 브라우저가 서버로부터 데이터를 읽음
 
----
- POST : 등록 및 변경
    - form 에 method를 post로 변경
    - 게시물을 등록한다.

----
- request response object
