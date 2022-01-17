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
    print(request.POST["name"])
    return HttpResponse("True")