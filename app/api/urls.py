from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, BookInstanceReadViewSet, BookInstanceCreateAPIView

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('booksinstances', BookInstanceReadViewSet)


urlpatterns = router.urls

urlpatterns += [
    path("bookinstanceadd/", BookInstanceCreateAPIView.as_view()),
]

