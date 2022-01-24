from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets,views
# from rest_framework.response import Response
from django.template.context_processors import csrf
from django.http import HttpResponse

from .models import Users,Question
from .serializers import QuestioinSerializer, UserSerializer

class Page1(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "online_Page1.html"
    serializer_class = UserSerializer
    queryset = Users.objects.none()
    def list(self,request):
        return render(request,"online_Page1.html")
    def create(self,request):
        return HttpResponse("<script>window.location.href='../main'</script>")
class RegisPage(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "online_regis.html"
    serializers = UserSerializer
    queryset = Users.objects.none()
    def list(self,request):
        _csrf = {}
        _csrf.update(csrf(request))
        return render(request,"online_regis.html")
    def create(self,request):
        try:
            queryset = Users.objects.get(account=request.POST["account"])
            return HttpResponse("<script>alert('此帳戶已被註冊');window.location.href='../main'</script>");
        except:
            usr = Users(account=request.POST["account"],password=request.POST["password"])
            usr.save()
            return HttpResponse("<script>alert('註冊成功');window.location.href='../main'</script>")

class Page2(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "online_Page2.html"
    serializers_class = UserSerializer
    queryset = Users.objects.none()
    def list(self,request): #HTTP GET
        return HttpResponse("<script>window.location.href='../main'</script>")
    def create(self,request): #HTTP POST
        try:
            queryset = Users.objects.get(account=request.POST["account"])
            try:
                queryset = Users.objects.get(account=request.POST["account"],password=request.POST["password"])
                response = render(request,"online_Page2.html")
                response.set_cookie("online_account",request.POST["account"])
                return response
            except:
                return HttpResponse("<script>alert('password error');window.location.href='../main'</script>")
        except:
            return HttpResponse("<script>window.location.href='../regis'</script>")

class Page3(viewsets.ModelViewSet):
    queryset = Question.objects.none()
    serializers_class = QuestioinSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "online_Page3.html"
    def list(self,request):
        try:
            queryset = Users.objects.get(account=request.COOKIES["online_account"])
            try:
                queryset = Question.objects.filter(account=request.COOKIES["online_account"]).last()
                return render(request,"online_Page3.html",{"question":f"{queryset.inputText}"})
            except:
                print("無法正常讀取問題庫")
                return HttpResponse("<script>window.location.href='../main'</script>")
        except:
            print("找不到此帳號")
            return HttpResponse("<script>window.location.href='../main'</script>")
    def create(self,request):
        try:
            acc = request.COOKIES["online_account"]
            print(request.POST["question"])
            question = Question(account=acc,inputText=request.POST["question"])
            question.save()
            return HttpResponse("<script>window.location.href='../result'</script>")
        except:
            print("無法儲存問題")
            return HttpResponse("<script>window.location.href='../main'</script>")