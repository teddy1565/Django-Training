from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import  HttpResponse
from django.views import csrf
from django.template.context_processors import csrf
from rest_framework.permissions import BasePermission
from os import path

from .models import  FilePathModel,FileNameModel
from .dynamic_url import updateRouteConfig
# Create your views here.

class Page1(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = FilePathModel.objects.none()
    template_name = "FinTech_Generator.html"
    permission_classes = [BasePermission]
    
    def list(self,request):
        _csrf = {}
        _csrf.update(csrf(request))
        return render(request,"FinTech_Generator.html")
    
    def create(self,request):
        try:
            generator_amount = request.POST["dataNum"]
            data_name = request.POST["fileName"]
            display_setting = request.POST["Display_Data_Amount"]
        except:
            return HttpResponse("Please fill all blank")
        
        fopenPath = f"{path.join(path.dirname(__file__),'FinTech_Generator')}";
        fopenPath = f"{path.join(fopenPath,data_name)}"
        print(fopenPath)
        try:
            fptr = open(fopenPath,"w")
            data = ""
            for i in range(1,int(generator_amount)+1):
                age = 25+((i+47*i)%45)
                revenue = 15000+((9797*i)%65000)
                money = 500+((797*i*i)%950000)
                debt = 2000+((97*i*i*i+97*i*i)%950000)
                loan = 4500+((20000+97*i*i)%35000)
                data = data+f"{i},{age},{revenue},{money},{debt},{loan}\n"
            fptr.write(data)
            fptr.close()
        except:
            return HttpResponse("FS Module Error")

        try:
            queryset = FilePathModel(path=fopenPath,displaySetting=display_setting)
            queryset.save()
        except:
            return HttpResponse("SQL Lite Error")
        
        try:
            queryset = FileNameModel(path=fopenPath,displaySetting=display_setting,fileName=data_name)
            queryset.save()
        except:
            return HttpResponse("SQL Lite Error")

        try:
            updateRouteConfig(path=fopenPath,fileName=data_name)
        except:
            return HttpResponse("Can't import urls")
        return HttpResponse("Hello world")

class fileURI():
    def generatorURI(path,fileName):
        class Tmp(viewsets.ModelViewSet):
            queryset = FilePathModel.objects.none()
            renderer_classes = [TemplateHTMLRenderer]
            template_name = "FinTech_Data.html"
            def list(self,request):
                try:
                    _path = path.replace("\n","")
                    _path = _path.replace("\\","\\\\")
                    print(_path)
                    fptr = open(_path,"r")
                    print(_path)
                    context = ""
                    for line in fptr.readlines():
                        context = context + line
                    fptr.close()
                    return render(request,"FinTech_Data.html",{"fileName":fileName,"context":context})
                except:
                    return HttpResponse("NoData")
        return Tmp
