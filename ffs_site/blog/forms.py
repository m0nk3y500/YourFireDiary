from django import forms
from .models import FFDiary

class PostForm(forms.ModelForm):

    class Meta:
        model = FFDiary
        fields = ['stichwort', 'date', 'content']
        labels = {
            'stichwort': 'Das Stichwort',
            'date': 'Datum',
            'content': 'Beschreibung'
        }

    