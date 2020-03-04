from rest_framework import serializers

from devices.models import Device, Measurement


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"
        read_only_fields = ["uuid", "time_created"]

    url = serializers.HyperlinkedIdentityField(view_name="device-detail")
    measurement_count = serializers.ReadOnlyField()


class DeviceCreateSerializer(DeviceSerializer):

    class Meta:
        model = Device
        fields = "__all__"
        read_only_fields = ["time_created"]


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = "__all__"
        read_only_fields = ["device", "time", "ph"]

    url = serializers.HyperlinkedIdentityField(view_name="measurement-detail")


class MeasurementCreateSerializer(MeasurementSerializer):

    class Meta:
        model = Measurement
        fields = "__all__"
        read_only_fields = ["time"]
