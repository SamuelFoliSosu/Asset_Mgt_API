from rest_framework import viewsets, permissions
from .models import OwnershipHistory
from .serializers import OwnershipHistorySerializer

class OwnershipHistoryViewSet(viewsets.ModelViewSet):
    queryset = OwnershipHistory.objects.all()
    serializer_class = OwnershipHistorySerializer
    permission_classes = [permissions.IsAuthenticated] 
