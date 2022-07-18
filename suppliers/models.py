from django.db import models

class Supplier(models.Model):
    # id = models.CharField(max_length=255) # necessário??
    cnpj = models.CharField(max_length=255, primary_key=True) #PK!
    created_at = models.DateTimeField()
    data_pagamento = models.CharField(max_length=255) # 2 em 1?
    data_validade = models.CharField(max_length=255) # 2 em 1?
    email = models.CharField(max_length=255)
    franquia = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255) # necessário?? ou dividir em first e last?
    senha = models.CharField(max_length=255)
    senha_provisoria = models.CharField(max_length=255)
    status = models.BooleanField()
    user = models.CharField(max_length=255)
    url_dashboard = models.CharField(max_length=255) # como automatizar para o PBI fornecê-lo???
