from django.urls import path
from .views import RegisterAPIView, LoginAPIView, DashboardAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterAPIView.as_view(), name='register_api'),
    path('api/auth/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/auth/dashboard/', DashboardAPIView.as_view(), name='dashboard_api'),

]