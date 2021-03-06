from __future__ import unicode_literals

from django.db import models
from user_info.models import user

# Create your models here.
def upload_location(instance, filename):
    return "./room_img/%s/%s" % (str(instance.room.User.id), filename)

class Room(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length= 10)
    price = models.IntegerField
    landmark = models.CharField(max_length=250, blank=True)
    long_term_lease = models.BooleanField()
    start_date = models.DateField()
    post_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.User.id) + " - " + self.description

class Room_img(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location, blank=True)

    def __str__(self):
        return str(self.room.id)
