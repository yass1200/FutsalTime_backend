from django.contrib import admin
from .models import FutsalField

@admin.register(FutsalField)
class FutsalFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "price_per_hour", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "location")
