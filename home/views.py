from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Article

def home(request):
    # return HttpResponse('<h1>qwertyu</h1>')
    articles = Article.objects.all()
    return render(request, 'home/index.html', {'articles':articles,})

def re_home(request):
    return HttpResponse('<h1>qwertyu</h1>')
