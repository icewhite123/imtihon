from django.shortcuts import render
from django.views.generic import  CreateView
from .models import Contact 
# Create your views here.
class Contact(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = "__all__"