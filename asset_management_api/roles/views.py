from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Role
from .serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can access
