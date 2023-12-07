# elevator_system/frontend/urls.py
from django.urls import path
from .views import elevator_status

urlpatterns = [
    path('', elevator_status, name='elevator_status'),
]
