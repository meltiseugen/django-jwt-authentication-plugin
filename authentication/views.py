from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers.read import CustomTokenObtainPairSerializer
from .serializers.write import UserSerializerWrite


class UserViewSet(
    viewsets.GenericViewSet,
):
    model = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializerWrite

    @action(detail=False, methods=['post'], permission_classes=(AllowAny,))
    def register(self, request):
        data = request.data

        serializer = self.get_serializer(data=data)
        if not serializer.is_valid(raise_exception=False):
            return Response({'errorMessage': 'User already exists'}, status=status.HTTP_409_CONFLICT)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
