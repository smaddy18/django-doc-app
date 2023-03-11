from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {"message": "Intégration bootstrap réussie !!!"}
    template = loader.get_template("listings/index.html")
    return HttpResponse(template.render(context, request))