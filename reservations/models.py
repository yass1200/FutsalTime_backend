from django.conf import settings
from django.db import models
from fields.models import FutsalField

class Reservation(models.Model):
    STATUS_CHOICES = (
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reservations")
    field = models.ForeignKey(FutsalField, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="CONFIRMED")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["field", "date", "start_time", "end_time"]),
        ]

    def __str__(self) -> str:
        return f"{self.user} -> {self.field} ({self.date} {self.start_time}-{self.end_time})"
