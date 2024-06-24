from django.contrib import admin
from filemanage.models import Directory, Document  # Corrigir importações

@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'owner')
    search_fields = ('name',)
    list_filter = ('owner',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'directory', 'owner')
    search_fields = ('file',)
    list_filter = ('owner', 'directory')
