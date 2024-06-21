from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document, Directory
from .forms import DocumentForm, DirectoryForm
from django.utils import timezone
from django.http import HttpResponse

@login_required
def file_list(request, directory_id=None):
    if directory_id:
        current_directory = get_object_or_404(Directory, id=directory_id, owner=request.user)
        documents = Document.objects.filter(owner=request.user, directory=current_directory)
        directories = Directory.objects.filter(owner=request.user, parent=current_directory)
    else:
        current_directory = None
        documents = Document.objects.filter(owner=request.user, directory__isnull=True)
        directories = Directory.objects.filter(owner=request.user, parent__isnull=True)
    return render(request, 'filemanage/file_list.html', {
        'documents': documents,
        'directories': directories,
        'current_directory': current_directory,
    })


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.uploaded_at = timezone.now()
            document.save()
            if document.directory:
                return redirect('file_list_with_directory', directory_id=document.directory.id)
            else:
                return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'filemanage/upload_file.html', {'form': form})


@login_required
def create_directory(request):
    if request.method == 'POST':
        form = DirectoryForm(request.POST)
        if form.is_valid():
            directory = form.save(commit=False)
            directory.owner = request.user
            directory.save()
            return redirect('file_list')
    else:
        form = DirectoryForm()
    return render(request, 'filemanage/create_directory.html', {'form': form})

@login_required
def download_file(request, file_id):
    document = get_object_or_404(Document, id=file_id, owner=request.user)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

@login_required
def download_folder(request, folder_id):
    folder = get_object_or_404(Directory, id=folder_id, owner=request.user)
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{folder.name}.zip"'
    return response
