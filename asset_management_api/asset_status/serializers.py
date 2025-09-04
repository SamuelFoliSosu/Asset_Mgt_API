from rest_framework import serializers
from .models import AssetStatus

class AssetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetStatus
        fields = "__all__"
