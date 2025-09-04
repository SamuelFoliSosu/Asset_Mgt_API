from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from asset_management_api.permissions import IsAdminOrReadOnly

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminOrReadOnly]
