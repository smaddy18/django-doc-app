from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
    form = forms.uploadData()
    context = {
        "title" : "Load data",
        "message": "Intégration bootstrap réussie !!!",
        "form": form,
    }
    return render(request, "listings/index.html", context)
