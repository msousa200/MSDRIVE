from django import forms
from .models import Document, Directory

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', 'directory')

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ('name', 'parent')
