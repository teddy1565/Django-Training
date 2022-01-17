# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import GameModel,GameContentModel
from .serializers import GameSerializer,GameContentSerializer
from django.shortcuts import render
from rest_framework import permissions
from django.http import HttpResponse

class GameHomePage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    template_name = "gameHomePage.html"
    queryset = GameModel.objects.none()

class GameContent(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = GameContentSerializer
    template_name = "gameContentPage.html"
    queryset = GameContentModel.objects.all().order_by("id")

def GameControl(request):
    if (request.GET["dp"] == request.GET["chose"]):
        return HttpResponse("true")
    else :
        return HttpResponse("false")