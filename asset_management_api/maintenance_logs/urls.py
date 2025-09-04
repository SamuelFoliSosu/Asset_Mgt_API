from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenanceLogViewSet

router = DefaultRouter()
router.register(r"", MaintenanceLogViewSet, basename="maintenance-log")

urlpatterns = [
    path("", include(router.urls)),
]
