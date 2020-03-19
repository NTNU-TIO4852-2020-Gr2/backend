from rest_framework import serializers

from devices.models import Device, Measurement, device_key_length


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"
        read_only_fields = ["uuid", "time_created"]

    key = serializers.CharField(write_only=True, min_length=device_key_length, max_length=device_key_length)
    url = serializers.HyperlinkedIdentityField(view_name="device-detail")


class DeviceCreateSerializer(DeviceSerializer):

    class Meta(DeviceSerializer.Meta):
        read_only_fields = ["time_created"]


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = "__all__"
        read_only_fields = ["device", "time", "ph", "temperature"]

    url = serializers.HyperlinkedIdentityField(view_name="measurement-detail")


class MeasurementCreateSerializer(MeasurementSerializer):

    class Meta(MeasurementSerializer.Meta):
        read_only_fields = ["time"]
