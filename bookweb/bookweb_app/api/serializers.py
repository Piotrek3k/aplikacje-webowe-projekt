from rest_framework import serializers
from bookweb_app.models import Book, Author, Review


    
        
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # book = BookSerializer(many=True,read_only=True)
    url= serializers.HyperlinkedIdentityField(view_name='author-info')
    book = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-info',
        
        )
    class Meta:
        model = Author
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    # book = BookSerializer(many=True,read_only=True)
    review_creator=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"
class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    #author = serializers.CharField(source=('author.firstName'+' '+'author.lastName'))
    author = serializers.CharField(source=('author.__str__'))
    class Meta:
        model = Book
        fields = "__all__"
