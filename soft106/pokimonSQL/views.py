from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Pokemon
from .serializers import HomePageSerializer
from rest_framework.renderers import TemplateHTMLRenderer

class pokemonHomePage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "pokemonHomePage.html"
    serializer_class = HomePageSerializer
    queryset = Pokemon.objects.none()
    def get(self,request):
        return render(request,"pokemonHomePage.html")