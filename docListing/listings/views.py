from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "title" : "Load data",
        "message": "Intégration bootstrap réussie !!!",
    }
    return render(request, "listings/index.html", context)