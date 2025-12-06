from django.urls import path
from .views import (
    AvailableSlotsView,
    ReservationCreateView,
    MyReservationsView,
    ReservationDetailView,
    ReservationCancelView,
)

urlpatterns = [
    path('available-slots/', AvailableSlotsView.as_view(), name='available-slots'),
    path('', ReservationCreateView.as_view(), name='reservation-create'),
    path('my-reservations/', MyReservationsView.as_view(), name='my-reservations'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation-cancel'),
]
