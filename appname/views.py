from django.shortcuts import render
from rest_framework.views import APIView
from.models import *
from django.http import JsonResponse
from django.views.generic import TemplateView
# Create your views here.

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
        try:
            user = User()
            user.image = img
            user.save()
            return JsonResponse({"status": "pass", "message": "Uploaded Successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "fail", "message": str(e)})


        

