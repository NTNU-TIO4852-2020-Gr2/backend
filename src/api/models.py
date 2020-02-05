import uuid
from django.db import models


class Device(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)


class Measurement(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    ph = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    turbidity = models.FloatField(blank=True, null=True)
    particle_density = models.FloatField(blank=True, null=True)
