from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from web.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("web.api_urls")),
    path("api/auth/", include("users.urls")),
    path("api/fields/", include("fields.urls")),
    path("api/reservations/", include("reservations.urls")),
    path("api/notifications/", include("notifications.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
