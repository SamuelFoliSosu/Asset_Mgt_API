from django.db import models

class AssetStatus(models.Model):
    # Name of the status (e.g., Active, In Repair, Retired)
    status_name = models.CharField(max_length=100)

    # Description to explain the status in detail
    description = models.TextField(blank=True)

    # When this record was created
    created_at = models.DateTimeField(auto_now_add=True)

    # When this record was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_name
