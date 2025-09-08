from rest_framework import serializers
from .models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='location.department.name', read_only=True)

    class Meta:
        model = Owner
        fields = [
            'id', 'location', 'location_name', 'department_name', 'name', 'owner_type',
            'contact_email', 'phone', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)
