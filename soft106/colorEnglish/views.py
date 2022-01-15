# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import GameModel,GameContentModel
from .serializers import GameSerializer,GameContentSerializer
from django.shortcuts import render
from rest_framework import permissions

class GameHomePage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    template_name = "gameHomePage.html"
    queryset = GameModel.objects.all().order_by("uid")
    def get(self,request):
        return render(request,"./gameHomePage.html")

class GameContent(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = GameContentSerializer
    template_name = "gameContentPage.html"
    queryset = GameContentModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        return render(request,"./gameContentPage.html")