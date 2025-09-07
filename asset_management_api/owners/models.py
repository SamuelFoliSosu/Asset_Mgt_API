from django.db import models
from locations.models import Location

class Owner(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='owners')
    name = models.CharField(max_length=150)
    owner_type = models.CharField(max_length=100)  # e.g., Individual, Department, Vendor
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name