from django.db import models
from django.contrib.auth.models import AbstractUser


class Supplier(AbstractUser):
    cnpj = models.CharField(editable=False, max_length=255, primary_key=True, unique=True) #PK!
    email = models.CharField(editable=True, max_length=255, unique=True)
    franquia = models.CharField(max_length=255)
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    password = models.CharField(editable=True, max_length=255, unique=False)
    password_provisional = models.CharField(max_length=255, null=True) # como fazer para ter duração definida??
    
    signature_created_at = models.DateTimeField(max_length=255)
    signature_status = models.BooleanField()
    signature_vality = models.CharField(max_length=255, null=True)
    
    url_dashboard = models.CharField(max_length=255) # como automatizar para o PBI fornecê-lo???
    
    username = models.CharField(max_length=255, null=True)
    username_created_at = models.DateTimeField()


class 
