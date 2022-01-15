from .views import GameHomePage,GameContent
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"",GameHomePage,basename="index")
router.register(r"game",GameContent,basename="game")

urlpatterns = router.urls