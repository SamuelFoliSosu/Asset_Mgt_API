from django.db import models
from assets.models import Asset
from asset_status.models import AssetStatus
from users.models import User

class AssetStatusHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='status_history')
    status = models.ForeignKey(AssetStatus, on_delete=models.CASCADE, related_name='asset_status_changes')
    changed_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='status_changes_made')
    change_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Status of {self.asset.asset_name} was changed to {self.status.status_name} on {self.change_date}"