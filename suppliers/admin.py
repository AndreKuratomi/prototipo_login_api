from django.contrib import admin
from django.contrib.auth.admin import SupplierAdmin
from .models import Supplier

admin.site.register(Supplier, SupplierAdmin)

# Register your models here.
