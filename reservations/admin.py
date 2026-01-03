from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "field", "date", "start_time", "end_time", "status", "created_at")
    list_filter = ("status", "date", "field")
    search_fields = ("user__username", "field__name")
