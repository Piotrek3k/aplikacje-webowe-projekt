from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    def save(self, **kwargs):
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError("You already have an account")
        
        new_user = User(email=self.validated_data['email'],username=self.validated_data['username'],password=self.validated_data['password'])
        # new_user.set_password(password=self.validated_data['password'])
        new_user.save()
        
        return new_user