from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import UserProfile


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['isBlockAdmin'] = self.user.profile.role == UserProfile.ROLE.BlockAdmin
        data['isBasicUser'] = self.user.profile.role == UserProfile.ROLE.BasicUser
        data['firstName'] = self.user.profile.display_user_surname
        data['lastName'] = self.user.profile.display_user_family_name
        return data
