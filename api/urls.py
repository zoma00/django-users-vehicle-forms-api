from django.urls import path, include
from rest_framework import routers
from .views import VehicleViewSet,VehicleTypeViewSet, ClientViewSet  # Assuming views.py in same directory

router = routers.DefaultRouter()
router.register('vehicle_types', VehicleTypeViewSet)
router.register('clients', ClientViewSet)
router.register('vehicle', VehicleViewSet)
# ... add other viewsets as needed

urlpatterns = [
    path('', include(router.urls)),
]