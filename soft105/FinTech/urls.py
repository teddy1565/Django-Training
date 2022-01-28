from rest_framework import routers
from django.urls import path,include

from .models import FileNameModel
from .views import Page1,fileURI
#from .refresh import urls
from threading import Timer
from .dynamic_url import downloadRouteConfig,clearRouteConfig
    

from os import path as PATH

router = routers.DefaultRouter()
router.register(r"index",Page1,basename="Page1")

counter = 0

urlList = []
urlList.append(path("",include(router.urls)))


Files = FileNameModel.objects.all()
for i in Files:
    counter+=1
    view = fileURI.generatorURI(path=i.path,fileName=i.fileName)
    view = view.as_view({"get":"list"})
    urlList.append(path(f"doc/{i.fileName}",view))

def dynamic_url():
    fileCofnig = downloadRouteConfig()
    if fileCofnig.__len__() == 2 :
        view = fileURI.generatorURI(path=fileCofnig[0],fileName=fileCofnig[1]).as_view({'get': 'list'})
        urlList.append(path(f"doc/{fileCofnig[1]}",view))
        clearRouteConfig()
    Timer(1,dynamic_url).start()

dynamic_url()
urlpatterns = urlList
