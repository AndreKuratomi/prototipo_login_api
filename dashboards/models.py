from django.db import models

from datetime import datetime, timedelta

from suppliers.models import Supplier


class Dashboard(models.Model):
    category = models.CharField(max_length=255)
    is_favorite = models.BooleanField()
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, unique=True)
    supplier_owner = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    last_clicked = models.DateTimeField(auto_now=True)
    
    dashboards = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="dashboards")
    favorites = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="favorite_dashboards")
    last_visited = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name="last_visited_dashboards")
