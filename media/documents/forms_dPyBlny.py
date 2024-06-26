from django import forms
from .models import Document, Directory

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', 'directory')

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super(DocumentForm, self).__init__(*args, **kwargs)
        
        if 'directory' in self.fields:
            if owner:
                self.fields['directory'].queryset = Directory.objects.filter(owner=owner)
            else:
                self.fields['directory'].queryset = Directory.objects.none()

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ('name', 'parent')

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super(DirectoryForm, self).__init__(*args, **kwargs)
        if owner:
            self.fields['parent'].queryset = Directory.objects.filter(owner=owner)
        else:
            self.fields['parent'].queryset = Directory.objects.none()


