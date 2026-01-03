from django.urls import path
from .views import NotificationListView, mark_all_read

urlpatterns = [
    path("", NotificationListView.as_view(), name="notifications_list"),
    path("mark-all-read/", mark_all_read, name="mark_all_read"),
]
