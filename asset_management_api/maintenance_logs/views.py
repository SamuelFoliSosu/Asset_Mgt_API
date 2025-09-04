from rest_framework import viewsets
from .models import MaintenanceLog
from .serializers import MaintenanceLogSerializer
from rest_framework.permissions import IsAuthenticated

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [IsAuthenticated]
