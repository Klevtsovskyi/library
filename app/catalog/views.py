from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Author, BookInstance


def index(request):
    book_num = Book.objects.all().count()
    author_num = Author.objects.all().count()
    bookinstance_num = BookInstance.objects.all().count()
    bookinstance_available_num = BookInstance.objects.filter(status__exact="a").count()
    context = {
        'book_num': book_num,
        'author_num': author_num,
        'bookinstance_num': bookinstance_num,
        'bookinstance_available_num': bookinstance_available_num,
    }
    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book

