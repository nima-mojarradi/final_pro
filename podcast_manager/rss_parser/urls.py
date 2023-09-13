from django.urls import path
from .views import ModelParserView

urlpatterns = [
    path('parser/', ModelParserView.as_view(), name='parser'),
]