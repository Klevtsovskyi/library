import uuid

from django.db import models

from library import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    summary = models.TextField(max_length=2000, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    genre = models.ManyToManyField('Genre', blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("a", "Доступно"),
        ("r", "Зарезервовано"),
        ("m", "На обслуговуванні"),
        ("o", "Орендована")
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="a")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=50, blank=True, null=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return self.book.title + ' ' + str(self.id)
