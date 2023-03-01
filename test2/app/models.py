from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    familliya=models.CharField(max_length=20)
    tel=models.CharField(max_length=30)

    
