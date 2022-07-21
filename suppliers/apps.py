from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Supplier


admin.site.register(Supplier, UserAdmin)
# class SuppliersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'suppliers'
