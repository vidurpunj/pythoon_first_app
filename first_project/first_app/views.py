from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>Hello World</em>")

def help(request):
    ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33, 'Vidur': 31}
    # return HttpResponse("<em>Help World</em>")
    return render(request, 'help.html', context=ages)
