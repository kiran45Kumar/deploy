from django.urls import path
from .views import *
urlpatterns = [
    path('upload_image/', UploadImage.as_view(),name='upload_image'),
    path('', ViewImage.as_view(),name='view_images'),
    path('delete/', DeleteImage.as_view(),name='delete_image')
]