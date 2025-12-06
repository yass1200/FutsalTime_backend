from django.urls import path
from .views import RegisterView, LoginView, LogoutView, GoogleAuthView, RefreshTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('google/', GoogleAuthView.as_view(), name='google-auth'),
    path('refresh/', RefreshTokenView.as_view(), name='token-refresh'),
]
