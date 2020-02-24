from base64 import b64decode

from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, ParseError
from rest_framework.utils import json

from devices.models import Device, Measurement

from .serializers import DeviceCreateSerializer, DeviceSerializer, MeasurementCreateSerializer, MeasurementSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return DeviceCreateSerializer
        return DeviceSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return MeasurementCreateSerializer
        return MeasurementSerializer

    @action(name="NB-IoT Engineering Webhook Endpoint", detail=False, methods=["post"])
    def nbiot_engineering(self, request):
        data = JSONParser().parse(request)
        if "messages" not in data or len(data["messages"]) == 0 or "payload" not in data["messages"][0]:
            return JsonResponse(status=400, data={"error": "Missing payload."})
        payload_encoded = data["messages"][0]["payload"]
        payload_string = b64decode(payload_encoded).decode("utf-8")
        try:
            payload_data = json.loads(payload_string)
        except ValueError as ex:
            raise ParseError("JSON parse error - {ex}".format(ex=ex))
        serializer = MeasurementCreateSerializer(data=payload_data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
