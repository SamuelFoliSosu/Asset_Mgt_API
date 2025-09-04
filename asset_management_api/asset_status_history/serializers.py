from rest_framework import serializers
from .models import AssetStatusHistory

class AssetStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetStatusHistory
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        # Ensure history is append-only (no updates to past records)
        return super().create(validated_data)
