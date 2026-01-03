from datetime import datetime
from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "user", "field", "date", "start_time", "end_time", "status", "created_at")
        read_only_fields = ("user", "status", "created_at")

    def validate(self, attrs):
        start = attrs.get("start_time")
        end = attrs.get("end_time")
        if start >= end:
            raise serializers.ValidationError("end_time must be after start_time.")
        return attrs
