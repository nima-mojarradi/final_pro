from django.urls import path
from .parser import ParsRssFeed
from .views import LikedPosts

urlpatterns = [
    path('parser/', ParsRssFeed.as_view(), name='parser'),
    path('likes/', LikedPosts.as_view(), name='likes'),
]