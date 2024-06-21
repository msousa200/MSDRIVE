from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Directory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='drive_children', on_delete=models.CASCADE)  
    owner = models.ForeignKey(User, related_name='drive_owned_directories', on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class Document(models.Model):
    directory = models.ForeignKey(Directory, related_name='drive_documents', on_delete=models.CASCADE)  
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='drive_owned_documents', on_delete=models.CASCADE) 

    def __str__(self):
        return self.title


