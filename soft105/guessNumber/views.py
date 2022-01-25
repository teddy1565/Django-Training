import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.context_processors import csrf
from .models import GuessNumberModel
# Create your views here.

class guessNumber(viewsets.ModelViewSet):
    queryset = GuessNumberModel.objects.none()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "guess_num.html"
    def list(self,request):
        _csrf = {}
        _csrf.update(csrf(request))
        response = render(request,"guess_num.html")
        return response
    def create(self,request):
        
        try:
            n = list(request.POST.keys())[0]
            queryset = GuessNumberModel.objects.filter(num=int(n)).last()
            if int(queryset.num) == int(n):
                return HttpResponse("true")
            else:
                return HttpResponse("false")
        except:
            return HttpResponse("false")

class GeneratorNumber(viewsets.ModelViewSet):
    queryset = GuessNumberModel.objects.none()

    def list(self,request):
        try:
            queryset = GuessNumberModel(num=int(request.GET["num"]))
            queryset.save()
            return HttpResponse("success")
        except:
            return HttpResponseBadRequest("Can't Query SQL")