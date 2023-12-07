from django.db import models

# Create your models here.

from django.db import models

class Elevator(models.Model):
    operational = models.BooleanField(default=True)
    in_maintenance = models.BooleanField(default=False)
    current_floor = models.IntegerField(default=1)
    moving_up = models.BooleanField(default=False)
    requests = models.ManyToManyField('Request', related_name='elevators')

class Request(models.Model):
    floor = models.IntegerField()
    direction = models.CharField(max_length=5, choices=[('up', 'Up'), ('down', 'Down')])
    served = models.BooleanField(default=False)
