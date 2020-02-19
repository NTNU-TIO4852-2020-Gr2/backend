from api.models import Measurement
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response




# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = '__all__'


# @api_view(['POST'])
# def register_measurement(request):
#     serializer = MeasurementSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response()
