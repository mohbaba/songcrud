from turtle import home
from django import views
from django.urls import path
from .apiviews import *

urlpatterns = [
    path('songs',song_list)
    # path('', SongApiView.as_view()),
    # path('artiste', ArtisteAPIView.as_view()),
]