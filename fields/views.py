from rest_framework import generics, permissions
from .models import FutsalField
from .serializers import FutsalFieldSerializer

class FieldListView(generics.ListAPIView):
    queryset = FutsalField.objects.filter(is_active=True)
    serializer_class = FutsalFieldSerializer
    permission_classes = (permissions.AllowAny,)


class FieldDetailView(generics.RetrieveAPIView):
    queryset = FutsalField.objects.filter(is_active=True)
    serializer_class = FutsalFieldSerializer
    permission_classes = (permissions.AllowAny,)
