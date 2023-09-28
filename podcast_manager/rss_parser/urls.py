from django.urls import path
from .parser import ParsRssFeed
from .views import LikedPodcasts

urlpatterns = [
    path('parser/', ParsRssFeed.as_view(), name='parser'),
    path('likes/', LikedPodcasts.as_view(), name='likes'),
]