from django.contrib import admin
from django.urls import path,include
from .views import pokemonHomePage,addPokemon,delPokemon

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r"homePage",HomePage.as_view(),basename="homepage")
router.register(r"homePage",pokemonHomePage,basename="hpp")

urlpatterns = [
    path("",include(router.urls)),
    path("control/add",addPokemon),
    path("control/del",delPokemon),
]