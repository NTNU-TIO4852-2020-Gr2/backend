from django.contrib.admin import register
from django.contrib.admin.options import ModelAdmin

from .models import Device, Measurement


@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display = ["uuid", "name", "latitude", "longitude"]


@register(Measurement)
class MeasurementAdmin(ModelAdmin):
    list_display = ["id", "device", "time", "ph"]
