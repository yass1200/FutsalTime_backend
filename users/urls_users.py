from django.urls import path
from .views import UserProfileView, UserBookingHistoryView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('booking-history/', UserBookingHistoryView.as_view(), name='booking-history'),
]
