from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from bookweb_app.user_account.views import Register_View, logout_view

urlpatterns = [
    path('auth/', obtain_auth_token, name="login"),
    path('register/', Register_View.as_view(), name="register"),
    path('logout/', logout_view, name="logout"),
]
