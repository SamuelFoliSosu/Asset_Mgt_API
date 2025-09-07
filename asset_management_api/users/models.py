from django.db import models
from departments.models import Department
from locations.models import Location
from roles.models import Role
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True,blank=True, related_name='users')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username