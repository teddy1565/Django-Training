from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import HomePageSerializer
from .models import HomePageModel
from rest_framework import viewsets
# Create your views here.

class HomePageView(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = HomePageSerializer
    template_name = "MLPage.html"
    queryset = HomePageModel.objects.none()