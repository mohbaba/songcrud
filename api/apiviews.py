from distutils.command.build_scripts import first_line_re
from rest_framework import generics
from musicapp.models import Song, Artiste
from .serializers import SongSerializer , ArtisteSerializer
from musicapp.views import *

# Create your views here.
class SongApiView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class ArtisteAPIView(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer