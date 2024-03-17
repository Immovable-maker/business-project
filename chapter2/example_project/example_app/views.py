from django.shortcuts import render

# # Create your views here.

from rest_framework.decorators import api_view, permission_classes
#view에 대한 인증이 필요 @api_view(['GET', 'POST']) 데코레이터와 'permission_classes': [] 옵션을 추가하여 기본 인증 요구 사항을 재정의할 수 있습니다.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)


def home(request):
   data = {
       'name': 'John Doe',
       'age': 25,
       'country': 'USA'
   }
   return render(request, 'myapp/home.html', context=data)
