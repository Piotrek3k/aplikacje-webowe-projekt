from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    def __str__(self):
        return self.firstName+" "+self.lastName
    
class Book(models.Model):
    title=models.CharField(max_length=50)   
    desc = models.CharField(max_length=1200)
    active=models.BooleanField(default=True)
    createdAt=models.DateTimeField(auto_now_add=True) 
    year=models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name="book")
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1,MaxValueValidator(10))])
    text = models.CharField(max_length=1200, null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="review")
    def __str__(self):
        return self.book.title