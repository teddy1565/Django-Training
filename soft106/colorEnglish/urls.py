from django.urls import path, include

from . import views

urlpatterns = [
   path("",views.GameHomePage),
   path("game",views.GameContext)
]