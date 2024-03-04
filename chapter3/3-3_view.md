Django의 뷰(Views)는 웹 요청을 받아 처리하고 웹 응답을 반환하는 Python 함수입니다. 

뷰는 데이터베이스로부터 데이터를 가져오고(모델을 통해), 필요한 작업을 수행한 후 데이터를 템플릿에 전달하여 렌더링


함수 기반 뷰(Function-Based Views, FBVs)
- 간단하고 직관적
- 유연하며, 복잡한 로직과 커스터마이징 가능
- 적은 보일러 플레이트

```
from django.http import HttpResponse
def hello_world(request):
    return HttpResponse("Hello, World!")

```


클래스 기반 뷰(Class-Based Views, CBVs)
- 내장 기능으로 존재
- 유지 보수성 향상
- 객체 목록 표시나 공통 패턴을 캡슐화 가능

```
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")

```

---
적어도 하나의 매개변수를 가져야함. request(현재 요청에 대한 메타데이터, http 헤더, 유저세부정보, 메서드 ,요청에 있는 param) 같은 것들이 들어옴

---
뷰를 애플리케이션에 연결하는 방법, URL 구성을 활용, 장고의 URL 라우팅을 활용하는 거야

```
from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view()),
]
```

---
제네릭 뷰들이 있어서 보일러플레이트 코드를 많이 줄여줌. 이게 강력한 기능 중에 하나래요

TemplateView : 주어진 템플릿을 렌더링합니다.
RedirectView : 다른 URL로 리디렉션을 제공합니다.
ListView : 객체 목록을 표시합니다.
DetailView : 단일 객체의 상세 뷰를 표시합니다.
CreateView, UpdateView, DeleteView : 객체를 생성, 업데이트, 삭제하기 위한 폼을 제공합니다.

```
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
```


---
마무리하며, Django 뷰는 어떤 Django 애플리케이션에 있어서 핵심적인 요소입니다. 사용자 요청을 처리하고 응답을 반환하는 로직을 정의하는 곳입니다. 함수 기반 뷰나 클래스 기반 뷰를 선택하는 것은 종종 달성하려는 작업의 복잡성에 따라 다릅니다. 기억해야 할 최종 목표는 이해하기 쉽고 유지 관리 가능하며 테스트하기 쉬운 뷰를 작성하는 것입니다.