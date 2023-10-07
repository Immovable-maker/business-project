## 목차
1. [프레임워크 설치](#pip를-사용하여-django-rest-framework-설치)

---
## pip를 사용하여 Django REST Framework 설치
pip install djangorestframework

이 명령은 Django REST Framework 패키지의 최신 버전과 필요한 종속성을 함께 설치합니다.

## Django REST Framework를 Django 프로젝트에 통합하기
Django 프로젝트의 example_project/settings.py 파일을 엽니다.

INSTALLED_APP과 아래의 등식을 확인합니다.

Django REST framework 공식 문서도 확인하기

## 간단한 REST API 생성

example_app/views.py 에 코드 추기

example_project/urls.py 에 코드 추기

실행안되면 interpreter path를 myenv걸로 잡아주기 django는 여기에만 깔려있음

python manage.py runserver 했을떄 api/hello path로 가면 에러가 남

example_app/views.py 파일 수정

## Django REST Framework 주요 구성 요소 개요

### 시리얼라이저(Serializers)
시리얼라이저는 Django 모델과 같은 **복잡한 데이터 유형**을 **JSON, XML 또는 기타 콘텐츠 유형**으로 변환하여 응답으로 렌더링하거나 클라이언트가 이해할 수 있는 형식으로 데이터를 **파싱하는 기능**을 제공합니다. 시리얼라이저는 들어오는 데이터를 파싱하고 복잡한 데이터 유형으로 다시 변환하는 **역 과정도 수행**할 수 있습니다.

```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    publication_date = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
```

### Views
Django REST Framework에서 뷰는 **HTTP 요청을 처리** 하고 **HTTP 응답을 반환하는 역할**을 담당합니다. 뷰는 종종 시리얼라이저를 사용하여 클라이언트가 이해할 수 있는 형식으로 데이터를 반환합니다. Django REST Framework는 APIView, GenericAPIView, ViewSet과 같은 여러 내장 뷰를 제공하여 일반적인 작업을 처리하여 **API 구축을 용이**하게 합니다.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Routers
Django REST Framework의 라우터는 **API 뷰에 대한 URL 패턴을 자동으로 생성**합니다. 라우터는 API **엔드포인트를 조직**하는 간단하고 일관된 방법을 제공하며 API의 버전을 관리하거나 네임스페이스 접두사를 적용하기 쉽게 합니다

```python
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
```

### 인증(Authentication)
Django REST Framework는 토큰 기반 인증, 세션 인증, OAuth2와 같은 다양한 인증 메커니즘을 지원하여 **인증된 사용자만 API에 액세스할 수 있도록 보장**합니다.

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # 뷰 코드...
```

### 권한(Permissions)
```python
from rest_framework.permissions import IsAdminUser

class BookListView(APIView):
    permission_classes = [IsAdminUser]

    # 뷰 코드...
    
```

### 쓰로틀링(Throttling)
쓰로틀링은 Django REST Framework의 중요한 기능으로, **API를 남용하거나 과도하게 사용하는 것으로부터 보호**합니다. 클라이언트가 특정 시간 프레임 내에서 요청할 수 있는 횟수를 제한할 수 있습니다. Django REST Framework는 여러 내장 쓰로틀링 클래스를 제공하며 사용자 정의 쓰로틀링 클래스를 만들어 요구 사항에 맞게 설정할 수도 있습니다.

```python
from rest_framework.throttling import UserRateThrottle

class BookListView(APIView):
    throttle_classes = [UserRateThrottle]

    # 뷰 코드...
```

### 페이지네이션(Pagination)
페이지네이션은 **대량의 데이터 집합 관리**하고 API의 성능을 향상시키는 데 중요합니다. Django REST Framework는 **limit/offset 페이지네이션**, 커서 페이지네이션 등 다양한 페이지네이션 스타일을 지원하며 전역적으로 또는 뷰별로 페이지네이션 설정을 구성할 수 있습니다.

```python
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookListView(APIView):
    pagination_class = CustomPagination

    # 뷰 코드...
```
### 필터(Filtering)
필터링은 **API에서 반환되는 데이터를 검색, 정렬 및 필터링**하는 데 도움을 주는 기능입니다. Django REST Framework는 Django Filter와 같은 인기있는 필터링 라이브러리와 통합되며 **쿼리 매개변수 필터링 및 결과 정렬**에 대한 내장 지원을 제공합니다.

```python
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

    # 뷰 코드...
```
### 예외(Exceptions)

Django REST Framework에는 유효성 검사 오류, 인증 실패, 권한 거부 등과 같은 **일반적인 API 오류를 처리**하는 일련의 내장 예외 클래스가 포함되어 있습니다. 이러한 예외는 **적절한 HTTP 상태 코드를 반환**하며 **더 자세한 오류 메시지를 반환**할 수 있도록 **사용자 정의**할 수 있습니다.
```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        custom_data = {'detail': response.data['detail']}
        response.data = custom_data
    return response
```

### 문서화(Documentation)
잘 문서화된 API는 개발자와 사용자 모두에게 중요합니다. Django REST Framework는 OpenAPI(이전 Swagger로 알려짐) 표준 지원 및 브라우저에서 작동하는 API 문서 생성 및 유지를 위한 여러 도구를 제공합니다.

Django REST Framework는 다양한 문서화 도구를 제공합니다. 가장 일반적인 방법은 **drf-yasg 라이브러리를 사용하여 OpenAPI 스펙을 생성하는 것**입니다. 자세한 예제 코드는 다음과 같습니다:

```python
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API for managing books",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True

,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 기존 URL 패턴들...
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
