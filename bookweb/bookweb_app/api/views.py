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









