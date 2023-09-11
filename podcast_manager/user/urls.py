from django.urls import path
from .views import RegisterUserView, user_login

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', user_login, name='login'),
]