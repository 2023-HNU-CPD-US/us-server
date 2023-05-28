from django import forms
from .models import Folder, Text

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['name', 'content']