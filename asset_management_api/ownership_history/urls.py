from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnershipHistoryViewSet

router = DefaultRouter()
router.register(r"", OwnershipHistoryViewSet, basename="ownership-history")

urlpatterns = [
    path("", include(router.urls)),
]
