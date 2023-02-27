from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    # return HttpResponse('<h1>qwertyu</h1>')
    time = datetime.datetime.now().time()
    # return render(request, 'home/index.html', {"time":time})
    return render(request, 'home/index.html')

def re_home(request):
    return HttpResponse('<h1>qwertyu</h1>')
