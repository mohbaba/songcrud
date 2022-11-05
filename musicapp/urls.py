from os import name
from pathlib import Path
from django.urls import path
from .views import songs , upload

urlpatterns = [
    path('', songs, name ='songs'),
    path('upload',upload, name='upload'),
]