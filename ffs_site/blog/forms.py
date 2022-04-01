from django import forms
from .models import FFDiary

class PostForm(forms.ModelForm):

    class Meta:
        model = FFDiary
        fields = ['stichwort', 'date', 'time', 'content']
        labels = {
            'stichwort': 'Stichwort',
            'date': 'Datum',
            'content': 'Beschreibung',
            'time' : 'Uhrzeit'
        }

    