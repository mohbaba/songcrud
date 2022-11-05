from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def songs(request):
    songs = Song.objects.all()
    # artists = Artiste.objects.all()
    return render(request, 'songs.html',{'songs':songs})

def upload(request):
    new_artist = Artiste.objects.get(pk=1)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        songname = request.POST['songname']
        likes = request.POST['likes']
        date = request.POST['date']
        
        new_artist.first_name = firstname
        new_artist.last_name = lastname
        new_artist.age = age
        # new_artist = Artiste.objects.create(first_name = firstname , last_name = lastname, age = age )
        # new_song = Song.objects.create(title= songname, likes=likes ,date_released=date)
        new_artist.save()