from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from django.template.context_processors import csrf
from django.http import HttpResponse

from .models import Users,Question
from .serializers import UserSerializer

class Page1(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "online_Page1.html"
    serializer_class = UserSerializer
    queryset = Users.objects.none()
    def get(self,request):
        csrf_temp = {}
        csrf_temp.update(csrf(request))
        return render(request,"online_Page1.html")