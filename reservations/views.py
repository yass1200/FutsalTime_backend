from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .models import Reservation
from .serializers import ReservationSerializer
from notifications.utils import create_notification

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Users can see only their reservations by default
        qs = Reservation.objects.all()
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        field = serializer.validated_data["field"]
        date = serializer.validated_data["date"]
        start_time = serializer.validated_data["start_time"]
        end_time = serializer.validated_data["end_time"]

        # Conflict check: overlapping confirmed reservations
        conflict = Reservation.objects.filter(
            field=field,
            date=date,
            status="CONFIRMED",
        ).filter(
            Q(start_time__lt=end_time) & Q(end_time__gt=start_time)
        ).exists()

        if conflict:
            raise ValueError("This time slot is already reserved.")

        reservation = serializer.save(user=self.request.user, status="CONFIRMED")
        create_notification(
            recipient=self.request.user,
            actor=self.request.user,
            verb=f"created a reservation for {field.name}",
            target=reservation,
        )

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        reservation = self.get_object()
        if reservation.status == "CANCELLED":
            return Response({"detail": "Already cancelled."})
        reservation.status = "CANCELLED"
        reservation.save()
        create_notification(
            recipient=request.user,
            actor=request.user,
            verb=f"cancelled a reservation for {reservation.field.name}",
            target=reservation,
        )
        return Response({"detail": "Reservation cancelled."})
