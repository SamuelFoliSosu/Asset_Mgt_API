from rest_framework import serializers
from .models import OwnershipHistory

class OwnershipHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipHistory
        fields = [
            "id", "asset", "from_owner", "to_owner",
            "transfer_date", "return_date",
            "condition_on_transfer", "comment",
            "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        if data["from_owner"] == data["to_owner"]:
            raise serializers.ValidationError(
                "from_owner and to_owner cannot be the same."
            )
        return data
