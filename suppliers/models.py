from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils import timezone
import uuid


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
    
    signature_created_at = models.DateTimeField(max_length=255, blank=True)
    signature_status = models.BooleanField(blank=True)
    signature_vality = models.CharField(max_length=255, blank=True)
    
    url_dashboard = models.CharField(max_length=255) # como automatizar para o PBI fornecê-lo???
    
    username = models.CharField(max_length=255, null=True, unique=False)
    username_created_at = models.DateTimeField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cnpj', 'first_name', 'last_name', 'password', 'password_provisional']
    objects = CustomUserManager()

