from pyexpat import model
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100, blank = True)
    last_name = models.CharField(max_length=100, blank = True)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=100, blank = True)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    
class Lyric(models.Model):
    content = models.TextField( blank = True)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)