from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Main
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    #path("login_failure/", LoginFailureView.as_view()),

    # Apps
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
]
