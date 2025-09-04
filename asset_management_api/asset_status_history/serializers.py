from rest_framework import serializers
from .models import AssetStatusHistory

class AssetStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetStatusHistory
        fields = [
            "id",
            "asset",
            "status",
            "changed_by_user",   #read-only
            "change_date",
            "comment",
        ]
        read_only_fields = ["id", "changed_by_user", "change_date"]

    def create(self, validated_data):
        # Inject the current request user automatically
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["changed_by_user"] = request.user
        return super().create(validated_data)
