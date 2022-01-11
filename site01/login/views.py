from django.shortcuts import render
from django.http import HttpResponse
from .models import USER


# Create your views here.
def index(request):
    """ 自製的登入介面 """
    page = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><form action="auth/" method="get"><input type="text" placeholder="account" name="account"><br><input type="password" placeholder="password" name="password"><br><button type="submit">登入</button></form></body</html>'
    return HttpResponse(page)

def form(request):
    account = request.GET["account"]
    password = request.GET["password"]
    print(USER.objects.all())
    try:
        u = USER.objects.get(usr=account,pwd=password)
        print(u)
        return HttpResponse("hello "+account)
    except:
        try:
            u = USER.objects.get(usr=account)
            return HttpResponse("password error")
        except:
            u = USER(usr=account,pwd=password)
            u.save()
            return HttpResponse("Hello new User : "+account)