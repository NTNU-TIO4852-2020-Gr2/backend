# import json
# import uuid
# from django.test import TestCase
# from rest_framework.test import APIClient
# from api.models import Device, Measurement


# class MeasurementTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.uuid = uuid.uuid4()
#         Device.objects.create(uuid=self.uuid)

#     def test_register_measurement(self):
#         measurement = json.dumps({
#             "device": str(self.uuid),
#             "ph": 1.0,
#             "temperature": 2.0,
#             "turbidity": 3.0,
#             "particle_density": 4.0})
#         response = self.client.post("/register", measurement, content_type="application/json")
#         self.assertEqual(response.status_code, 200)
