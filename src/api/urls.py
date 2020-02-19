from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from rest_framework.schemas import get_schema_view

from common.permissions import AllowAll
from common.routers import PublicDefaultRouter

from .views import DeviceViewSet, MeasurementViewSet

admin.site.site_header = settings.SITE_NAME
schema_view = get_schema_view(title=settings.APP_NAME, permission_classes=[AllowAll])

router = PublicDefaultRouter()
router.register("devices", DeviceViewSet)
router.register("measurements", MeasurementViewSet)

urlpatterns = [
    path("schema/", schema_view, name="schema"),
    path("v0/", include(router.urls)),
    path("", RedirectView.as_view(url="v0/", permanent=False)),
]
