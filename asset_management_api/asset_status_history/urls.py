from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AssetStatusHistoryViewSet

router = DefaultRouter()
router.register(r'', AssetStatusHistoryViewSet, basename='assetstatushistory')

urlpatterns = [
    path('', include(router.urls)),
]
