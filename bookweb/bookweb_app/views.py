""" from django.shortcuts import render
from bookweb_app.models import Book
from django.http import JsonResponse
def book_list(request):
    books = Book.objects.all()
    data={
        'books': list(books.values())} 
    
    return JsonResponse(data)
    
def book_detail(request, book_id):
    book=Book.objects.get(id=book_id)
    data={
         'name': book.name,
         'description': book.description,
         'active': book.active} 
    print(book.name)
    return JsonResponse(data)
    
# Create your views here. """
