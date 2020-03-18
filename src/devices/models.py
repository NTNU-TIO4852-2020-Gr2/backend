import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string


def get_random_string_64():
    return get_random_string(length=64)


class Device(models.Model):

    class Meta:
        ordering = ("name",)

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    key = models.CharField(default=get_random_string_64, max_length=64, validators=[MinLengthValidator(64)])
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{uuid} ({name})".format(uuid=self.uuid, name=self.name)

    @property
    def measurements(self):
        return Measurement.objects.filter(device=self)

    @property
    def measurement_count(self):
        return self.measurements.count()


class Measurement(models.Model):

    class Meta:
        ordering = ("-time",)

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{device} - {time}".format(device=self.device, time=self.time)
