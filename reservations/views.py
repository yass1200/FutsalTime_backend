from datetime import time

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import Reservation
from .serializers import ReservationSerializer
from fields.models import FutsalField


class AvailableSlotsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        # Basic stub: you can implement real slot generation later
        date = request.GET.get('date')
        field_id = request.GET.get('field')
        if not date or not field_id:
            return Response(
                {'detail': 'date and field parameters are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # For now, just return an empty list to show the shape.
        return Response({'date': date, 'field': field_id, 'available_slots': []})


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyReservationsView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by('-date', '-start_time')


class ReservationDetailView(generics.RetrieveAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationCancelView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
        except Reservation.DoesNotExist:
            return Response({'detail': 'Reservation not found.'}, status=status.HTTP_404_NOT_FOUND)

        if reservation.status == 'cancelled':
            return Response({'detail': 'Already cancelled.'}, status=status.HTTP_400_BAD_REQUEST)

        reservation.status = 'cancelled'
        reservation.save()
        return Response({'detail': 'Reservation cancelled.'})
