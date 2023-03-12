from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
import json
from . import functions

def index(request):
    form = forms.uploadData()
    context = {
        "title" : "Load data",
        "message": "Intégration bootstrap réussie !!!",
        "form": form,
    }
    return render(request, "listings/index.html", context)

def displayDocs(request):
    #myData
    if(request.method == "POST"):
        file = request.FILES["file"]
        
        # Enregistrement du fichier dans un fichier temporaire
        with open("ressources/temp.json", "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
                
        # Lecture du fichier temporaire
        with open("ressources/temp.json") as jsonFile:
            myData = json.load(jsonFile)
            
        # Isoler les différents clusters
        clusters = []
        for item in myData:
            if(item["Cluster"] not in clusters):
                clusters.append(item["Cluster"])
        
        # Trier les données par ordre inverse du nombre de fois cité
        myData = sorted(myData, key=functions.getCitationCount, reverse=True)
        clusters = sorted(clusters)
    
        context = {
            "title" : "Data displaying",
            "data" : functions.refactorDataKeys(myData),
            "clusters" : clusters,
        }
        
        return render(request, "listings/display.html", context)
    else:
        return HttpResponseRedirect('forms/')