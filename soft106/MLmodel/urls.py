from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
pattern = [
    path("",include(router.urls)),
]