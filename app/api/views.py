from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from .serializers import BookSerializer, AuthorSerializer, BookInstanceSerializer
from catalog.models import Book, Author, BookInstance


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookInstanceReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

    def get_queryset(self):
        queryset = BookInstance.objects.all()
        book_id = self.request.query_params.get('book_id', None)
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        return queryset


class BookInstanceCreateAPIView(CreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

