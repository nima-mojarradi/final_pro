from django.urls import path
from .views import ParsRssFeed

urlpatterns = [
    path('parser/', ParsRssFeed.as_view(), name='parser'),
]