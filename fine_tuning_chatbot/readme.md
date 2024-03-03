python3 -m venv backend_env 이걸로 backend_env 폴더 만들어졌고

fine_tuning_chatbot 루트 폴더에서 source backend_env/bin/activate 로 실행해, 

pip install django djangorestframework django-cors-headers 이걸로 또 설치는 해놨어 CORS 대비

python -m django --version 나 pip list로 환경 잘 되어있나 보고

---

django-admin startproject backend 이걸로 backend 폴더 만들어

cd backend로 이동하고 python manage.py runserver

그 폴더에서 그대로 python manage.py startapp fine_tuning_chatbot

으로 생성하였음
---

settings.py 파일은 Django 프로젝트에서 INSTALLED_APPS 설정은 프로젝트에 설치된 애플리케이션을 정의하는 목록입니다. 목록의 각 항목은 프로젝트에 특정 기능을 제공하는 Django 애플리케이션을 나타냅니다.

여기에 rest_framework, fine_tuning_chatbot 넣음 세부사항은 backend/backend/settings.py 확인

---

backend/backend/urls.py 파일을 열고 urlpatterns 목록을 다음과 같이 업데이트합니다:

backend/fine_tuning_chatbot/ 디렉토리 내에 urls.py라는 새로운 파일을 생성하고 다음 코드를 추가합니다:

backend/fine_tuning_chatbot/views.py 파일에 다음 코드를 추가합니다:

python manage.py runserver 로 중간점검 하고 http://127.0.0.1:8000/ 방문하면됨. /api/hello 쳐서 패스 추가후 되는지 확인

-- 

현재 개발 서바나 PC에서 프론트엔드는 http://localhost:3000에서 호스팅되고 백엔드는 http://127.0.0.1:8000에서 호스팅됩니다 프론트엔드가 백엔드에 API 요청을 보낼 때, 이는 Cross-Origin 요청으로 간주됩니다. 

웹 브라우저는 보안을 위해 기본적으로 Cross-Origin 요청을 차단합니다. 따라서 우리는 백엔드를 구성하여 프론트엔드가 요청을 보낼 수 있도록 해야 합니다. 이는 아래와 같이 CORS를 백엔드에서 설정을 해 주어야 합니다. 

settings.py에 APP이랑 주석 보면 1~6까지 새로적음 

(이거 근데 pip install django-cors-headers 이거 해야되네, INSTALLED APP에 추가하려면 이렇게 해줘야되네)

---

필요한 테이블을 생성하기 위해 데이터베이스 마이그레이션을 수행합니다: python manage.py migrate

---

frontend 폴더 chatbot 루트폴더에 만들고 들어가서 npx create-next-app fine-tuning-chatbot

npm install로 종속성 설치하고 npm run dev로 실행

---

거기에서 app/하위에 있는것들이 원래 실행되어서 default_page 폴더로 옮겼음

근데 일단 pages/ 라는 폴더를 만들었고 그 밑에 index.tsx만들었음

---

이거 고쳤음 backend에서 CORS 오류 때문에 안되는것 같길래
https://velog.io/@lob3767/Django-CORS-%EC%84%A4%EC%A0%95



