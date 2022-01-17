from django.contrib import admin
from django.urls import path,include
from .views import pokemonHomePage

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r"homePage",HomePage.as_view(),basename="homepage")
router.register(r"homePage",pokemonHomePage,basename="hpp")

urlpatterns = [
    path("",include(router.urls)),
    #path("homePage/",pokemonHomePage),
]