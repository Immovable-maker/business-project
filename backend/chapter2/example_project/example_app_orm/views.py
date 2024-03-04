from django.shortcuts import render
from example_app_orm.models import Author , Book
# Create your views here.

def home(request):
    # 객체 생성 및 데이터베이스에 저장
    author = Author(name='John Doe', age=30)
    author.save()

    book = Book(title='My Book', author=author)
    book.save()

    # 데이터베이스에서 객체 검색
    books = Book.objects.all()  # 모든 책 검색
    book = Book.objects.get(title='My Book')  # 특정 책 검색

    # 객체 업데이트
    book.title = 'New Book Title'
    book.save()

    # 객체 삭제
    book.delete()

    return render(request, 'home.html')
