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
    
    class Meta:
        model = Review
        fields = "__all__"
class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = "__all__"
# """ def name_length_validator(val):
#     if(len(val))<2:
#         raise serializers.ValueError("Name must be at least 2 characters long")
#     elif(len(val))>50:
#         raise serializers.ValueError("Name is too long")
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length_validator])
#     desc = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Book.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.desc = validated_data.get('desc',instance.desc)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance  """