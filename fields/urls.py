from rest_framework.routers import DefaultRouter
from .views import FutsalFieldViewSet

router = DefaultRouter()
router.register(r"", FutsalFieldViewSet, basename="fields")

urlpatterns = router.urls
