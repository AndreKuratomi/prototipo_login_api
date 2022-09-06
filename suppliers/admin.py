from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Supplier

admin.site.register(Supplier, UserAdmin)

# Register your models here.
