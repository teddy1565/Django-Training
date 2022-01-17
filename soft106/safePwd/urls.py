from rest_framework import routers
from django.urls import path,include
from .views import MainPage
router = routers.DefaultRouter()
router.register(r"main",MainPage,basename="main")

urlpatterns = [
    path("",include(router.urls)),
]