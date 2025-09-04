from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetStatusViewSet

router = DefaultRouter()
router.register(r'asset-statuses', AssetStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
