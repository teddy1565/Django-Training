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
        return HttpResponse("新增失敗")
    except:
        queryset = Pokemon(name=request.POST["name"],serial=request.POST["serial"],position=request.POST["position"],pokemonType=request.POST["pokemonType"])
        queryset.save()
        return HttpResponse("新增成功")

def delPokemon(request):
    permission_classes = [permissions.AllowAny]
    try:
        queryset = Pokemon.objects.get(serial=request.POST["serial"])
        queryset.delete()
        return HttpResponse("刪除成功")
    except:
        return HttpResponse("刪除失敗")

def queryPokemon(request):
    if request.POST["position"] != "" and request.POST["pokemonType"] != "":
        queryset = Pokemon.objects.get(position=request.POST["position"],pokemonType=request.POST["pokemonType"])
        print(queryset)
        return HttpResponse(queryset)
    elif request.POST["position"] != "" and request.POST["pokemonType"] =="":
        queryset = Pokemon.objects.get(position=request.POST["position"])
        print(queryset)
        return HttpResponse(queryset)
    elif request.POST["position"] == "" and request.POST["pokemonType"] !="":
        queryset = Pokemon.objects.get(pokemonType=request.POST["pokemonType"])
        print(queryset)
        return HttpResponse(queryset)
    else:
        return HttpResponse("沒有符合條件的資料")

def list(request):
    permission_classes = [permissions.AllowAny]
    queryset = Pokemon.objects.all().order_by("date")
    data = f"<pre>uid\t中文名稱\t出沒地點\t屬性\t圖鑑編號\t建立日期</pre><br>"
    for i in queryset:
        data = data + f"{i}<br>"
    return HttpResponse(data)