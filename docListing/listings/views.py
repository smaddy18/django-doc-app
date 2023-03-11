from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpResponse('<h1>Hello Django!</h1>')