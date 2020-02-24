from django.contrib.admin import register
from django.contrib.admin.options import ModelAdmin

from .models import Device, Measurement


@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display = ["uuid", "name", "latitude", "longitude"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["uuid", "time_created"]
        else:
            return []


@register(Measurement)
class MeasurementAdmin(ModelAdmin):
    list_display = ["id", "device", "time", "ph"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["device", "time", "ph"]
        else:
            return []
