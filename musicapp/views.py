
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import SongsForm
from .models import *


# Create your views here.
def songs(request):
    songs = Song.objects.all()
    # artists = Artiste.objects.all()
    return render(request, 'songs.html',{'songs':songs})

def upload(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    age = request.POST['age']
    songname = request.POST['songname']
    likes = request.POST['likes']
    dates = request.POST['dates']
    
    artist = Artiste(first_name = firstname,last_name = lastname, age = age)
    artist.save()
    song = Song(
        title = songname,
        date_released = dates,
        likes = likes,
        artiste_id = Artiste.objects.get(first_name = firstname,last_name = lastname, age = age)
        )
    song.save()
    return redirect('/')