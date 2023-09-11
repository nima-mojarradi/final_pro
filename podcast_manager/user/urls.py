from django.urls import path
from .views import RegisterUserView, user_login, user_logout

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]