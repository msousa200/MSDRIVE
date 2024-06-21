from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:directory_id>/', views.file_list, name='file_list_directory'),
    path('create_directory/', views.create_directory, name='create_directory'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('download-folder/<int:folder_id>/', views.download_folder, name='download_folder')
]