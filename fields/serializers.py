from rest_framework import serializers
from .models import FutsalField

class FutsalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutsalField
        fields = ("id", "name", "location", "price_per_hour", "open_time", "close_time", "is_active")
