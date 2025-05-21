from django.shortcuts import render
from rest_framework.views import APIView
from.models import *
from django.http import JsonResponse
from django.views.generic import TemplateView
# Create your views here.
from PIL import Image
import os
from django.core.exceptions import ValidationError
from .models import User  # assuming User model has an `image` field

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import User
class ViewImage(TemplateView):
    template_name = 'app/image.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imgs = User.objects.all()
        context['imgs'] = imgs
        return context

class UploadImage(APIView):
    def post(self, request):
        img = request.FILES.get('img')

        # Check if file exists
        if not img:
            return JsonResponse({"status": "fail", "message": "No image uploaded."})

        # Validate file extension
        valid_extensions = ['.jpg', '.jpeg', '.png']
        ext = os.path.splitext(img.name)[1]
        if ext.lower() not in valid_extensions:
            return JsonResponse({"status": "fail", "message": "Unsupported file extension."})

        # Validate file size (e.g., max 2MB)
        if img.size > 2 * 1024 * 1024:
            return JsonResponse({"status": "fail", "message": "Image too large. Max size is 2MB."})

        # Validate actual image content
        try:
            image = Image.open(img)
            image.verify()  # Will throw exception if invalid
        except Exception:
            return JsonResponse({"status": "fail", "message": "Uploaded file is not a valid image."})

        # Save the user image
        try:
            user = User()
            user.image = img
            user.save()
            return JsonResponse({"status": "pass", "message": "Uploaded successfully."})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "fail", "message": str(e)})


        

