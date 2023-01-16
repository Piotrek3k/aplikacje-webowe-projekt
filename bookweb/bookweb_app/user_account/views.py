from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from bookweb_app.user_account.serializers import RegistrationSerializer
from bookweb_app.user_account.create_token import create_auth_token
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

class Register_View(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        response_data = {}
        if serializer.is_valid():
            new_user = serializer.save()
 
            token = Token.objects.get_or_create(user=new_user)[0]
            response_data['response'] = 'User {name} registered successfully'.format(
                name=new_user.username)
            #response_data['username'] = new_user.username
            #response_data['email'] = new_user.email
            response_data['token'] = token.key
        else:
            response_data = serializer.errors
        return Response(response_data)

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    