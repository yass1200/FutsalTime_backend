from rest_framework import serializers
from .models import FutsalField

class FutsalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutsalField
        fields = '__all__'
