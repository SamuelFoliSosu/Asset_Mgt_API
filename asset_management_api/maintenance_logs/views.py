from rest_framework import viewsets, permissions
from .models import MaintenanceLog
from .serializers import MaintenanceLogSerializer

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
