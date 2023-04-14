from django.db import models

# Create your models here.
class ManagerUser(models.Model):
    password_hash = models.CharField(max_length=512)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

class PlayerUser(models.Model):
    password_hash = models.CharField(max_length=512)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    manager = models.ForeignKey(ManagerUser, on_delete=models.CASCADE)