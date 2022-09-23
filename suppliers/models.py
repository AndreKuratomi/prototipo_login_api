from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils import timezone

from datetime import datetime, timedelta

import uuid
import ipdb

accurate_time = datetime.now() - timedelta(hours=3)
log_adm_view = datetime.strftime(accurate_time, "%d-%m-%Y às %H:%M:%S")

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Email não fornecido!')

        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Supplier(AbstractUser):
    cnpj = models.CharField(editable=False, max_length=255, primary_key=True) #READ-ONLY. Talvez dê problema
    email = models.EmailField(editable=True, max_length=255, unique=True)
    franquia = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    password = models.CharField(editable=True, max_length=255, unique=False)
    password_provisional = models.CharField(default=uuid.uuid4, max_length=255, blank=True) # como fazer para ter duração definida??

    signature_created_at = models.DateTimeField(default=accurate_time, max_length=255, null=False)
    signature_vality = models.CharField(max_length=255)
    
    is_admin = models.BooleanField()
    is_super_user = models.BooleanField()
    
    # url_dashboard = models.URLField(max_length=255) # como automatizar para o PBI fornecê-lo???
    
    username = models.CharField(max_length=255, null=True, unique=False)
    username_created_at = models.DateTimeField(default=accurate_time)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cnpj', 'first_name', 'last_name', 'password', 
    # 'signature_status', 'signature_vality', 
    'is_super_user', 'is_admin'
    # 'url_dashboard', 
    'username']
    objects = CustomUserManager()


class LoggedSupplier(models.Model):
    date_logged = models.CharField(max_length=255)
    supplier = models.ForeignKey("Supplier", blank=True, on_delete=models.CASCADE, related_name="login_dates")
