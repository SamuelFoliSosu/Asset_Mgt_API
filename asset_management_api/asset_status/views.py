from rest_framework import viewsets, permissions
from .models import AssetStatus
from .serializers import AssetStatusSerializer

class AssetStatusViewSet(viewsets.ModelViewSet):
    queryset = AssetStatus.objects.all()
    serializer_class = AssetStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
