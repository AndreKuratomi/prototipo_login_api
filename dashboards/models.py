from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

from datetime import datetime, timedelta

from suppliers.models import Supplier


class Dashboard(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=255)
    is_favorite = models.BooleanField()
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, unique=True)
    supplier_owner = models.CharField(max_length=255)

    created_at = models.DateTimeField(default=datetime.now() - timedelta(hours=3))

    last_clicked = models.DateTimeField(default=datetime.now() - timedelta(hours=3))
    
    supplier1 = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="dashboards")
    supplier2 = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="favorite_dashboards")
    supplier3 = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="last_visited_dashboards")
    # REQUIRED_FIELDS = ['__all__']
