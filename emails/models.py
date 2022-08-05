from django.db import models

class Mail(models.Model):
    subject_supplier = models.CharField(max_length=255)
    subject_admin = models.CharField(max_length=255)
    message_supplier = models.TextField()
    message_admin = models.TextField()
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    fail_silently = models.BooleanField(default=False)

