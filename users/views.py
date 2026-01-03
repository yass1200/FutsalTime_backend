from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id: int):
    target = generics.get_object_or_404(User, pk=user_id)
    if target == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=400)
    request.user.following.add(target)
    return Response({"detail": f"You are now following {target.username}."})

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id: int):
    target = generics.get_object_or_404(User, pk=user_id)
    request.user.following.remove(target)
    return Response({"detail": f"You unfollowed {target.username}."})
