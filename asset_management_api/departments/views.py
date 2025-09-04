from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer
from asset_management_api.permissions import IsAdminOrReadOnly

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]
