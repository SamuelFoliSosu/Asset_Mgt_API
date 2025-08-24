from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of department
    created_at = models.DateTimeField(auto_now_add=True) # Time created
    updated_at = models.DateTimeField(auto_now=True) #Time updated

    def __str__(self):
        return self.name
