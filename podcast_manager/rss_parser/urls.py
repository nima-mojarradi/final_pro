from django.urls import path
from .views import ParsRssFeed, LikeView

urlpatterns = [
    path('parser/', ParsRssFeed.as_view(), name='parser'),
    path('like/', LikeView.as_view(), name='likes')
]