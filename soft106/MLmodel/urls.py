from django.contrib import admin
from django.urls import path,include

from .views import HomePageView

from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"main",HomePageView)

urlpatterns = [
    path("",include(route.urls)),
]