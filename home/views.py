from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Article
from .forms import NameForm

def home(request):
    # return HttpResponse('<h1>qwertyu</h1>')
    print(request.method)
    # request.
    articles = Article.objects.all()

    my_form = NameForm()

    return render(request, 'home/index.html', {'articles':articles, 'my_form':my_form})

def re_home(request):

    return HttpResponse('<h1>qwertyu</h1>')
