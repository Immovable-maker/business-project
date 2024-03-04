Django 프로젝트는 전체 웹 애플리케이션을 나타내며, 앱은 프로젝트 내에서 특정한 기능을 제공하는 모듈입니다.

최상위 backend 폴더의 project 확인, 프로젝트가 여러개의 앱을 포함가능

프로젝트 
- 관리 작업을 위한 명령 줄 유틸리티인 manage.py 파일
- 전체 Django 프로젝트의 구성을 담고 있는 settings.py 파일
- URL을 기반으로 웹 요청을 라우팅하는 urls.py 파일 
- 그리고 WSGI-나 ASGI-호환 웹 서버가 프로젝트를 제공하는 데 사용하는 wsgi.py 또는 asgi.py 파일 등이 있습니다.

프로젝트 생성
```django-admin startproject your_project_name```

앱
- 데이터베이스 스키마를 위한 models.py 파일 
- 비즈니스 로직을 담당하는 views.py 파일
- 그리고 단위 테스트를 위한 tests.py 파일로 구성됩니다. 
- 앱은 앱별 URL 라우팅을 위한 urls.py 파일 
- Django 관리자 인터페이스를 구성하기 위한 admin.py 파일 
- Django 폼을 정의하기 위한 forms.py와 같은 추가 파일을 포함할 수도 있습니다.


