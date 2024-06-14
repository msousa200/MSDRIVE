from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Directory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    directory = models.ForeignKey(Directory, related_name='documents', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)  # Use default=timezone.now para preencher automaticamente
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name



