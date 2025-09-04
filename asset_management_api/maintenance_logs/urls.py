from rest_framework.routers import DefaultRouter
from .views import MaintenanceLogViewSet

router = DefaultRouter()
router.register(r'maintenance-logs', MaintenanceLogViewSet, basename='maintenance-log')

urlpatterns = router.urls
