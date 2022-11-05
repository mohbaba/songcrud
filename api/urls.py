from turtle import home
from django import views
from django.urls import path
from .apiviews import *

urlpatterns = [
    path('', SongApiView.as_view()),
]