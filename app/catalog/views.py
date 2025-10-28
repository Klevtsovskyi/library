from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .forms import BookInstanceForm
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

class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author


@permission_required(("add_bookinstance", "change_bookinstance"))
def book_instance(request, pk):
    book = get_object_or_404(Book, id=pk)
    uid = request.GET.get("uid", None)
    if uid:
        obj = get_object_or_404(BookInstance, id=uid)
    else:
        obj = None

    if request.method == "POST":
        form = BookInstanceForm(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.book = book
            instance.save()
            return redirect("book_detail", pk=pk)
    else:
        form = BookInstanceForm(instance=obj)

    return render(request, 'catalog/book_instance.html', {"form": form, "book": book})
