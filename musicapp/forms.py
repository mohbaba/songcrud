from dataclasses import fields
from django import forms
from .models import *

class SongsForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'title','date_released', 'artiste_id', 'likes'
        ]