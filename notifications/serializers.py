from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ("id", "verb", "timestamp", "is_read", "target_repr")

    def get_target_repr(self, obj):
        return str(obj.target) if obj.target else None
