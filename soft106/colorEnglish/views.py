# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import GameModel
from .serializers import GameSerializer

class GameHomePage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "gameHomePage.html"
    queryset = GameModel.objects.all()
    def get(self,request):
        return Response(request,"./gameHomePage.html")