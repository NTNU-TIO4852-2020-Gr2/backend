import uuid

from django.db import models


class Device(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return super(Device).__str__()


class Measurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ("-time",)

    def __str__(self):
        return "{device} - {time}".format(device=self.device, time=self.time)
