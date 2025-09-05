# assets/serializers.py
from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"

    def validate(self, data):
        # Example: ensure current_value is not negative
        if data.get("current_value", 0) < 0:
            raise serializers.ValidationError(
                {"current_value": "Current value cannot be negative."}
            )
        return data
