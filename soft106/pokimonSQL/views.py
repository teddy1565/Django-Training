from turtle import position
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Pokemon
from .serializers import HomePageSerializer,addPokemonSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions
from django.template import Context,loader
from django.template.context_processors import csrf

class pokemonHomePage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "pokemonHomePage.html"
    serializer_class = HomePageSerializer
    queryset = Pokemon.objects.none()
    def get(self,request):
        csrf_variable = {}
        csrf_variable.update(csrf(request))
        return render(request,"pokemonHomePage.html")

def addPokemon(request):
    permission_classes = [permissions.AllowAny]
    queryset = Pokemon.objects.all()
    
    try:
        queryset.get(serial=request.POST["serial"])
        return HttpResponse("False")
    except:
        queryset = Pokemon(name=request.POST["name"],serial=request.POST["serial"],position=request.POST["position"],pokemonType=request.POST["pokemonType"])
        queryset.save()
        return HttpResponse("True")

def delPokemon(request):
    permission_classes = [permissions.AllowAny]
    try:
        queryset = Pokemon.objects.get(serial=request.POST["serial"])
        queryset.delete()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def queryPokemon(request):
    if request.POST["position"] != "" and request.POST["pokemonType"] != "":
        queryset = Pokemon.objects.get(position=request.POST["position"],pokemonType=request.POST["pokemonType"])
        print(queryset)
        return HttpResponse("True")
    elif request.POST["position"] != "" and request.POST["pokemonType"] =="":
        queryset = Pokemon.objects.get(position=request.POST["position"])
        print(queryset)
        return HttpResponse("True")
    elif request.POST["position"] == "" and request.POST["pokemonType"] !="":
        queryset = Pokemon.objects.get(pokemonType=request.POST["pokemonType"])
        print(queryset)
        return HttpResponse("True")
    else:
        return HttpResponse("False")