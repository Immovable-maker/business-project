from django.urls import path
from .views import create_book, book_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', create_book, name='create_book'),
    path('list/', book_list, name='book_list'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# +static은 단순히 개발 중에 미디어파일을 제공하기 위해서 