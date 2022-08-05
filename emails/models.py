from django.db import models

class UserMail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    fail_silently = models.BooleanField(default=False)


class AdminMail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    fail_silently = models.BooleanField(default=False)
