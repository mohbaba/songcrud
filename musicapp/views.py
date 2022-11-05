from django.http import HttpResponse
from django.shortcuts import render
from .forms import SongsForm
from .models import *


# Create your views here.
def songs(request):
    songs = Song.objects.all()
    # artists = Artiste.objects.all()
    return render(request, 'songs.html',{'songs':songs})

def upload(request):
    context ={}

    # add the dictionary during initialization
    form = SongsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    
    return render(request, 'songs.html',context)