from .views import Page1, Page2, RegisPage, Page3
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"main",Page1,basename="main")
router.register(r"textInput",Page2,basename="textInput")
router.register(r"regis",RegisPage,basename="regis")
router.register(r"result",Page3,basename="result")

urlpatterns = [
    path("",include(router.urls)),
]