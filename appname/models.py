from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    image = CloudinaryField('image')