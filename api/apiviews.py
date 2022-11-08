from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from musicapp.models import Song, Artiste
from .serializers import SongSerializer , ArtisteSerializer


# Create your views here.
@api_view(['GET','POST'])
def song_list(request):
    
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many= True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)





# METHOD TWO
# class SongApiView(generics.ListAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
    
    
    
# class ArtisteAPIView(generics.ListAPIView):
#     queryset = Artiste.objects.all()
#     serializer_class = ArtisteSerializer
    
#     def artiste_response(request):
#         if request.method == 'GET':
#             artists = Artiste.objects.all()
#             serializer = ArtisteSerializer(artists, many = True)
#             return JsonResponse(serializer.data, safe=False)
        
#         elif request.method == 'POST':
#             data = None