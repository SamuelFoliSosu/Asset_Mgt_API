from rest_framework import serializers
from .models import MaintenanceLog
from datetime import date

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = "__all__"

    def validate(self, data):
        # Maintenance date cannot be in the future
        if data["maintenance_date"] > date.today():
            raise serializers.ValidationError("Maintenance date cannot be in the future.")

        # Next due date must be after the maintenance date
        if data.get("next_due_date") and data["next_due_date"] <= data["maintenance_date"]:
            raise serializers.ValidationError("Next due date must be after the maintenance date.")

        return data
