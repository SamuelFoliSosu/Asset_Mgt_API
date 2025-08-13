from django.db import models
from assets.models import Asset
from owners.models import Owner

class OwnershipHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    from_owner = models.ForeignKey(Owner, related_name='ownership_from', on_delete=models.SET_NULL, null=True, blank=True)
    to_owner = models.ForeignKey(Owner, related_name='ownership_to', on_delete=models.SET_NULL, null=True, blank=True)
    transfer_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    condition_on_transfer = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Asset {self.asset.asset_name}'s ownership was transfered from {self.from_owner} to {self.to_owner}"
