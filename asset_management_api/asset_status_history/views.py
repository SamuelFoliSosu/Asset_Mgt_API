from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import AssetStatusHistory
from .serializers import AssetStatusHistorySerializer
from rest_framework.permissions import IsAuthenticated

class AssetStatusHistoryViewSet(viewsets.ModelViewSet):
    queryset = AssetStatusHistory.objects.all().order_by("-change_date")
    serializer_class = AssetStatusHistorySerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Prevent updates to history
        return Response(
            {"detail": "Updating status history is not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def partial_update(self, request, *args, **kwargs):
        # Prevent partial updates too
        return Response(
            {"detail": "Updating status history is not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def destroy(self, request, *args, **kwargs):
        # Prevent deletion of history
        return Response(
            {"detail": "Deleting status history is not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )