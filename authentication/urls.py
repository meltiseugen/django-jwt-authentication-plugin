from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    UserViewSet,
    CustomTokenObtainPairView
)


router = routers.DefaultRouter()
router.register('users', UserViewSet, 'auth-users')

urlpatterns = [
    path('auth/', include(router.urls)),
    path('auth/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_obtain_refresh'),
]
