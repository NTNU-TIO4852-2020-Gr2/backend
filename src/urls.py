from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    # Main
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    # path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.ico", permanent=True)),
    path('api/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('devices/', include('devices.urls')),
    path('', RedirectView.as_view(pattern_name="dashboard", permanent=False), name='home'),
]
