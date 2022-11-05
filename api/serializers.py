from dataclasses import fields
from rest_framework import serializers
from musicapp.models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title','date_released', 'likes', 'artiste_id')