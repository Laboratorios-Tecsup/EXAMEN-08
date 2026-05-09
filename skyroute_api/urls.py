from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, AirlineViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet, basename='flights')
router.register('airlines', AirlineViewSet, basename='airlines')

urlpatterns = router.urls