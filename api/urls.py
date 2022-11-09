from rest_framework.urlpatterns import format_suffix_patterns
from django import views
from django.urls import path
from .apiviews import *

urlpatterns = [
    path('songs',song_list),
    path('artistes', artiste_list),
    path('songs/<int:id>',song_detail), 
    # path('', SongApiView.as_view()),
    # path('artiste', ArtisteAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)