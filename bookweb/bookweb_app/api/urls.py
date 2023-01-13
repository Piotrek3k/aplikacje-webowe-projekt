from django.urls import path, include
from bookweb_app.api.views import ReviewList,ReviewInfo,AuthorList,AuthorInfo,BookList,BookInfo,ReviewCreate

urlpatterns = [
    path('booklist/',BookList.as_view(), name='book-list'),
    path('books/<int:pk>', BookInfo.as_view(), name='book-info'),
    path('authorlist/',AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorInfo.as_view(), name='author-info'),
    path('authors/<int:pk>/review',ReviewList.as_view(), name='review-list'),
    path('authors/review/<int:pk>',ReviewInfo.as_view(), name='review-info'),
    path('authors/<int:pk>/create',ReviewCreate.as_view(), name='review-create'),
]