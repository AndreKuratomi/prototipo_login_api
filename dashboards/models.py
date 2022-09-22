from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

from datetime import datetime, timedelta

local_time = datetime.now() - timedelta(hours=3)

# class CustomUserManager(BaseUserManager):
class Dashboard(models.Model):
    id = models.IntegerField(editable=False, unique=True, primary_key=True)
    category = models.Charfield(max_length=255)
    is_favorite = models.BooleanField()
    name = models.Charfield(max_length=255)
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(default=local_time)
    
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="dashboards")

    # REQUIRED_FIELDS = ['__all__']
