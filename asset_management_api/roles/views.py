from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer
from asset_management_api.permissions import IsAdminOrReadOnly

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]
