from django.conf import settings
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def create_book(request):
    # base_url = settings.BASE_URL
    base_url = settings.MEDIA_URL

    if(request.method == 'POST'):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/create_book.html', {'form': form, 'base_url' : base_url,})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})