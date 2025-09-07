from django.db import models
from locations.models import Location
from owners.models import Owner

class Asset(models.Model):
    asset_type = models.CharField(max_length=100)
    asset_name = models.CharField(max_length=150)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='assets')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='assets')
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=50, blank=True)
    operating_system = models.CharField(max_length=50, blank=True)
    cpu = models.CharField(max_length=50, blank=True)
    memory = models.CharField(max_length=50, blank=True)
    hard_disk_space = models.CharField(max_length=50, blank=True)
    screen_size = models.CharField(max_length=50, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    useful_life_years = models.PositiveIntegerField(blank=True, null=True)
    salvage_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    assigned_staff_name = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.asset_name