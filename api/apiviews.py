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
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET','POST'])
def artiste_list(request):
    
    if request.method == 'GET':
        artists = Artiste.objects.all()
        serializer = ArtisteSerializer(artists, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtisteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def artiste_detail(request,id):
    
    try:
        artist = Artiste.objects.get(pk = id)
    except Artiste.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = ArtisteSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artist, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        artist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET','PUT','DELETE'])
def song_detail(request,id):
    try:
        song = Song.objects.get(pk=id)
        serializer = SongSerializer(song,data = request.data)
    except Song.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
        
        




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