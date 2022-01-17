from django.urls import path, include
from .views import GameControl, GameHomePage,GameContent
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"homePage",GameHomePage,basename="homePage")
router.register(r"game",GameContent,basename="game")

urlpatterns = [
    path("",include(router.urls)),
    path("control/",GameControl),
]