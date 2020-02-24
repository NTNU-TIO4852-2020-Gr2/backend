from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Main
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    # path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.ico", permanent=True)),
    path('analysis/', include('analysis.urls')),
    path('api/', include('api.urls')),
    path('devices/', include('devices.urls')),
    path('', include('home.urls')),
]
