from rest_framework import generics
from musicapp.models import Song, Artiste
from .serializers import SongSerializer

# Create your views here.
class SongApiView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer