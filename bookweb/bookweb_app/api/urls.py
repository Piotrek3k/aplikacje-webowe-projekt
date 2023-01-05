from django.urls import path, include
from bookweb_app.api.views import book_list, book_info, author_info, author_list, review_info, review_list

urlpatterns = [
    path('booklist/',book_list, name='book-list'),
    path('books/<int:pk>', book_info, name='book-info'),
    path('authorlist/',author_list, name='author-list'),
    path('authors/<int:pk>', author_info, name='author-info'),
    path('reviewlist/',review_list, name='review-list'),
    path('review/<int:pk>',review_info, name='review-info'),
]