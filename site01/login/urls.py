from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="login"),
    path("auth/",views.form,name="auth"),
]