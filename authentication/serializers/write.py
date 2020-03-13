from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from .read import UserProfileSerializerWrite


class UserSerializerWrite(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.is_active = validated_data['is_active']
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_active']
