from rest_framework import routers
from .views import guessNumber,GeneratorNumber
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r"index",guessNumber,basename="index")
router.register(r"generate",GeneratorNumber,basename="GeneratorNumber")

urlpatterns = [
    path("",include(router.urls)),
]