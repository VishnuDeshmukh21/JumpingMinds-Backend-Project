# elevator_system/elevator_system/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from elevator.views import ElevatorViewSet, RequestViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
