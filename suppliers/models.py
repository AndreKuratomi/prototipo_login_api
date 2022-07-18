from django.db import models

class Supplier(models.Model):
    cnpj = models.CharField(max_length=255, primary_key=True) #PK!
    email = models.CharField(max_length=255)
    franquia = models.CharField(max_length=255)
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_provisional = models.CharField(max_length=255) # como fazer para ter duração definida??
    signature_created_at = models.CharField(max_length=255)
    signature_status = models.BooleanField()
    signature_vality = models.CharField(max_length=255)
    url_dashboard = models.CharField(max_length=255) # como automatizar para o PBI fornecê-lo???
    username = models.CharField(max_length=255)
    username_created_at = models.DateTimeField()
