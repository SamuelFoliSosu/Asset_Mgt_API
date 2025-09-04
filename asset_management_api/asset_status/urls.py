from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AssetStatusViewSet

router = DefaultRouter()
router.register(r'', AssetStatusViewSet, basename='assetstatus')

urlpatterns = [
    path('', include(router.urls)),
]
