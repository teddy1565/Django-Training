from django.contrib import admin
from django.urls import path,include

from rest_framework import routers

route = routers.DefaultRouter()

urlpatterns = route.urls