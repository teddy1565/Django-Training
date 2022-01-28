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
        display_data=""
        try:
            fptr = open(fopenPath,"w")
            data = ""
            counter=0
            for i in range(1,int(generator_amount)+1):
                age = 25+((i+47*i)%45)
                revenue = 15000+((9797*i)%65000)
                money = 500+((797*i*i)%950000)
                debt = 2000+((97*i*i*i+97*i*i)%950000)
                loan = 4500+((20000+97*i*i)%35000)
                data = data+f"{i},{age},{revenue},{money},{debt},{loan}\n"
                if counter < int(display_setting):
                    display_data = display_data + f"{i},{age},{revenue},{money},{debt},{loan}\n"
                    counter = counter+1
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
        return render(request,"FinTech_Generator_result.html",{"URI":f"http://localhost:8000/FinTech/doc/{data_name}","N":f"{display_setting}","data":display_data})

class Page2(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = FileNameModel.objects.none()
    permission_classes = [BasePermission]
    template_name = "FinTech_evaluate.html"

    def list(self,request):
        _csrf = {}
        _csrf.update(csrf(request))
        return render(request,"FinTech_evaluate.html")
    
    def create(self,request):
        uri = request.POST["URI"]
        _uri = request.POST["URI"]
        threshold = request.POST["Threshold"]
        amount = request.POST["Amount"]
        uri = uri.replace("http://localhost:8000/FinTech/doc/","")
        rootPath = path.dirname(__file__)
        thePath = path.join(rootPath,"FinTech_Generator",uri)
        point = []
        result = []
        response = ""
        try:
            fptr = open(thePath)
            for line in fptr.readlines():
                payload = line.split(",")
                payload = 50*float(payload[0])/75-(50*float(payload[1]))/80000-(60*(float(payload[2])-float(payload[3])))/60000+(40*float(payload[4]))/50000
                point.append(int(payload))
            fptr.close()
        except:
            return HttpResponse("Can't read File")
        point.sort()
        for i in range(int(amount)):
            tmp = point.pop()
            if tmp >= int(threshold):
                result.append(tmp)
        try:
            for r in result:
                fptr = open(thePath)
                for line in fptr.readlines():
                    line = line.replace("\n","")
                    payload = line.split(",")
                    payload = 50*float(payload[0])/75-(50*float(payload[1]))/80000-(60*(float(payload[2])-float(payload[3])))/60000+(40*float(payload[4]))/50000
                    if int(payload) == r:
                        response = response+line+f",{r}"+"\n\n"
                        break
                fptr.close()
        except:
            return HttpResponse("Can't read File")
        return render(request,"FinTech_evaluate_result.html",{"URI":_uri,"N":amount,"data":response})

class fileURI():
    def generatorURI(path,fileName):
        class Tmp(viewsets.ModelViewSet):
            queryset = FilePathModel.objects.none()
            def list(self,request):
                try:
                    _path = path.replace("\n","")
                    _path = _path.replace("\\","\\\\")
                    print(_path)
                    fptr = open(_path,"r")
                    print(_path)
                    context = ""
                    for line in fptr.readlines():
                        context = context + line + "\n"
                    fptr.close()
                    return HttpResponse(context)
                except:
                    return HttpResponse("NoData")
        return Tmp
