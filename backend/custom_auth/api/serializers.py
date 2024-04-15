from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class LoginSerializer(serializers.Serializer):
    """
    The login serializer validates user authentication data.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user or not user.is_active:
                raise serializers.ValidationError('Invalid credentials.')
        else:
            raise serializers.ValidationError(
                'Email and password are required.'
            )
        return data


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for validating email and confirmation code.
    """
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'confirmation_code')
