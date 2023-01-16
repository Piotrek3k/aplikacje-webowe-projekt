from bookweb_app.models import Book, Author, Review
from bookweb_app.api.serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from bookweb_app.api.permissions import *

class ReviewList(generics.ListCreateAPIView):
    def get_queryset(self):
        id = self.kwargs['pk']
        return Review.objects.filter(book=id)
    serializer_class = ReviewSerializer
    permission_classes = [AdminPerm]

class ReviewInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AdminPerm]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_creator__username', 'rating']

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book=Book.objects.get(pk=pk)
        
        filtered_review = Review.objects.filter(review_creator=self.request.user,book=book)
        if(filtered_review.exists()):
            # raise serializers.ValidationError("Review already exists")
            raise ValidationError('Review already exists')
        
        rating = serializer.validated_data['rating']
        print(rating)
        book.no_ratings += 1
        print(book.no_ratings)
        # calculate average rating
        book.avg = (book.avg* (book.no_ratings-1) + rating) / book.no_ratings    
        book.save()
        serializer.save(book=book, review_creator=self.request.user)
    
class ReviewDelete(generics.DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [UserReviewPerm]
  
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_destroy(self, serializer):

        reviewid = self.kwargs.get('pk')
        review = Review.objects.get(pk=reviewid)
        book=Book.objects.get(pk=review.book.id)
        print(str(reviewid) + "reviewid")
        print(book.id)
        
        rating = review.rating
        # calculate average rating
        print(book.avg)
        print(book.avg* book.no_ratings)
        book.avg = ((book.avg* book.no_ratings)- rating) / (book.no_ratings-1)  
        print(book.avg)
        book.no_ratings-=1
        book.save()
        review.delete()
        
    
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AdminPerm]
    filter_backends = [filters.SearchFilter]
    search_fields = ['lastName', 'firstName']

class AuthorInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AdminPerm]
    
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AdminPerm]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class BookInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AdminPerm]









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
