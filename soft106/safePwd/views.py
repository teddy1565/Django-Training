from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from .models import PWD
from .serializers import PasswordSerializer
from django.template.context_processors import csrf
from django.http import HttpResponse
# Create your views here.

class MainPage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "password.html"
    serializer_class = PasswordSerializer
    queryset = PWD.objects.none()
    def get(self,request):
        csrf_variable = {}
        csrf_variable.update(csrf(request))
        return render(request,"password.html")
    
def regis(request):
    print(request)
    return HttpResponse("HI",200)