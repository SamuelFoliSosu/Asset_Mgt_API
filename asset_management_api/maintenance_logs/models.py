from django.db import models
from assets.models import Asset
from users.models import User  # assuming you have a Users app

class MaintenanceLog(models.Model):
    # The asset that was maintained or repaired
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    
    # The user who performed the maintenance (e.g., IT Manager)
    performed_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Date when maintenance happened
    maintenance_date = models.DateField()
    
    # Type of maintenance (e.g., repair, servicing)
    maintenance_type = models.CharField(max_length=100)
    
    # Current status of the maintenance (e.g., completed, pending)
    status = models.CharField(max_length=50)
    
    # When the next maintenance is due (optional)
    next_due_date = models.DateField(null=True, blank=True)
    
    # Cost of the maintenance or repair
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Action taken during maintenance (e.g., replaced part)
    action_taken = models.TextField(blank=True)
    
    # Description of the issue or problem addressed
    issue_description = models.TextField(blank=True)
    
    # Timestamp when this record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when this record was last updated
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Maintenance was done on {self.asset.asset_name} on {self.maintenance_date}"
