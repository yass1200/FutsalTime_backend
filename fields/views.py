from datetime import datetime, timedelta, time
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import FutsalField
from .serializers import FutsalFieldSerializer
from reservations.models import Reservation

class FutsalFieldViewSet(viewsets.ModelViewSet):
    queryset = FutsalField.objects.all()
    serializer_class = FutsalFieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["get"])
    def availability(self, request, pk=None):
        field = self.get_object()
        date_str = request.query_params.get("date")
        if not date_str:
            return Response({"detail": "Provide ?date=YYYY-MM-DD"}, status=400)

        try:
            day = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"detail": "Invalid date format. Use YYYY-MM-DD"}, status=400)

        start_dt = datetime.combine(day, field.open_time)
        # If close_time is midnight, treat as next day 00:00
        close_time = field.close_time
        end_dt = datetime.combine(day, close_time)
        if close_time == time(0, 0):
            end_dt = datetime.combine(day + timedelta(days=1), time(0, 0))

        slots = []
        cursor = start_dt
        while cursor < end_dt:
            next_cursor = cursor + timedelta(hours=1)
            slots.append({"start": cursor.isoformat(), "end": next_cursor.isoformat(), "available": True})
            cursor = next_cursor

        # Mark reserved slots
        reservations = Reservation.objects.filter(field=field, date=day, status="CONFIRMED")
        for r in reservations:
            for s in slots:
                s_start = datetime.fromisoformat(s["start"])
                s_end = datetime.fromisoformat(s["end"])
                if not (r.end_time <= s_start.time() or r.start_time >= s_end.time()):
                    s["available"] = False

        return Response({"field": field.id, "date": date_str, "slots": slots})
