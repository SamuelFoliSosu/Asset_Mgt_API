from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetStatusHistoryViewSet

router = DefaultRouter()
router.register(r'asset-status-history', AssetStatusHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
