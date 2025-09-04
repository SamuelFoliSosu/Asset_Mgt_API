from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Asset
from .serializers import AssetSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    # Enable filtering + search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Filtering by FK relations
    filterset_fields = ['location', 'owner_id', 'location__department_id']

    # Search across text fields
    search_fields = ['asset_name', 'serial_number', 'model']
