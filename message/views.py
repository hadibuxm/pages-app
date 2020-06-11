from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Messages
# Create your views here.
class MessageView(ListView):
    model=Messages
    template_name='message.html'
