from .views import GameHomePage,GameContent
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"homePage",GameHomePage,basename="index")
router.register(r"game",GameContent,basename="game")

for i in router.urls:
    print(i)
urlpatterns = router.urls