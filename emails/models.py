from django.db import models

class UserMail(models.Model):
    subject = models.CharField(255)
    message = models.TextField()
    sender = models.CharField(255)
    receiver = models.CharField(255)
    fail_silently = models.BooleanField(default=False)


class AdminMail(models.Model):
    subject = models.CharField(255)
    message = models.TextField()
    sender = models.CharField(255)
    receiver = models.CharField(255)
    fail_silently = models.BooleanField(default=False)
