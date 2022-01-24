from .views import Page1
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"main",Page1,basename="main")

urlpatterns = [
    path("",include(router.urls)),
]