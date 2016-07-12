from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    email = models.CharField(max_length=50)
    alias = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    avatar = models.CharField(max_length=1000,  blank=True)
    cellNumber = models.CharField(max_length=10, blank=True)


