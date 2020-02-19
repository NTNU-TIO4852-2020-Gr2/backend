from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    # Main
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    # path("login_failure/", LoginFailureView.as_view()),
    # path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.ico", permanent=True)),
    path("", RedirectView.as_view(url="api/", permanent=False)),

    # Apps
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
]
