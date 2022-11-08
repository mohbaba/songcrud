from dataclasses import fields
from rest_framework import serializers
from musicapp.models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','date_released', 'likes', 'artiste_id']
        
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id','first_name','last_name','age']