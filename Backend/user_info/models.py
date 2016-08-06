from __future__ import unicode_literals
from django.db import models

# Create your models here.
def upload_location(instance, filename):
    return "../%s/%s" % (instance, filename)

class user(models.Model):
    email = models.CharField(max_length=50)
    alias = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    avatar = models.ImageField(upload_to=upload_location, default='../media/None/icon-user-default.png')
    cellNumber = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.email + " - " + self.alias + " " + str(self.pk)
