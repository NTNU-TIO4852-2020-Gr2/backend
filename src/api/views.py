from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Device, Measurement
from .serializers import DeviceSerializer, MeasurementSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    @action(name="NB-IoT Engineering Webhook Endpoint", detail=False, methods=["post"])
    def nbiot_engineering(self, request):
        #serializer = PasswordSerializer(data=request.data)
        #if serializer.is_valid():
        #    user.set_password(serializer.data['password'])
        #    user.save()
        #    return Response({'status': 'password set'})
        print(request.data)
        response_date = {
            "status": "success",
            "data": request.data,
        }
        return Response(response_date)
