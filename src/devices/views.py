from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Device, Measurement


def device_list(request):
    context = {}
    context["devices"] = Device.objects.all()
    context["breadcrumblist"] = [
        ("Home", "/"),
        ("Devices", reverse("device_list")),
    ]
    return render(request, "devices/list.html", context)


def device_detail(request, device_uuid):
    device = get_object_or_404(Device, uuid=device_uuid)

    context = {}
    context["device"] = device
    context["measurements"] = device.measurements
    context["breadcrumblist"] = [
        ("Home", "/"),
        ("Devices", reverse("device_list")),
        ("Device {name}".format(name=device.name), reverse("device_detail", args=[device_uuid])),
    ]
    return render(request, "devices/detail.html", context)
