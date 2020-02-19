from django.contrib.admin import register
from django.contrib.admin.options import ModelAdmin

from .models import Device, Measurement


@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display = ["__all__"]


@register(Measurement)
class MeasurementAdmin(ModelAdmin):
    list_display = ["__all__"]
