from django.urls import path, include
urlpatterns = [
 path('api/users/', include('users.urls')),
 path('api/fields/', include('fields.urls')),
 path('api/reservations/', include('reservations.urls')),
 path('api/notifications/', include('notifications.urls')),
]
