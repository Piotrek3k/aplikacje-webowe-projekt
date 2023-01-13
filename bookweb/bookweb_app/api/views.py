from bookweb_app.models import Book, Author, Review
from bookweb_app.api.serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.exceptions import ValidationError

class ReviewList(generics.ListCreateAPIView):
    def get_queryset(self):
        id = self.kwargs['pk']
        return Review.objects.filter(book=id)
    serializer_class = ReviewSerializer

class ReviewInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        id = self.kwargs['pk']
        book=book.objects.get(pk=id)
        review_creator=self.request.user
        filtered_review = Review.objects.filter(review_creator=review_creator,book=book)
        if(filtered_review.exists()):
            # raise serializers.ValidationError("Review already exists")
            raise ValidationError('You have already reviewed this book')
        
        
        serializer.save(review_creator=review_creator, book=book)
    
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer









# @api_view(['GET','POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','POST'])
# def review_list(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# @api_view(['GET','POST'])       
# def author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True,context={'request': request})
        
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def book_info(request, pk):
    
#     if request.method == 'GET':
#         try:
#             book=Book.objects.get(id=pk)
#         except Book.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(book)
#         return Response(serializer.data) 
#     if request.method == 'PUT':
#         book=Book.objects.get(id=pk)
#         serializer = BookSerializer(book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#          book=Book.objects.get(id=pk)
#          book.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)
     
# @api_view(['GET','PUT','DELETE'])
# def review_info(request, pk):
    
#     if request.method == 'GET':
#         try:
#             review=Review.objects.get(id=pk)
#         except Review.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data) 
#     if request.method == 'PUT':
#         review=Review.objects.get(id=pk)
#         serializer = ReviewSerializer(review,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#          review=Review.objects.get(id=pk)
#          review.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','PUT','DELETE'])
# def author_info(request, pk):
#     if request.method == 'GET':
#         try:
#             author=Author.objects.get(id=pk)
#         except Author.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = AuthorSerializer(author,context={'request': request})
#         return Response(serializer.data) 
#     if request.method == 'PUT':
#         author=Author.objects.get(id=pk)
#         serializer = AuthorSerializer(author,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#          author=Author.objects.get(id=pk)
#          author.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)
