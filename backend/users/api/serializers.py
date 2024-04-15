from djoser.serializers import UserCreateSerializer, UserSerializer

from users.models import User


class CustomUserSerializer(UserSerializer):
    """
    Custom serializer for user data.
    """

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name'
        )


class CustomCreateUserSerializer(UserCreateSerializer):
    """
    Custom serializer for creating user instances.
    """
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'password'
        )
        required_fields = (
            'email', 'password'
        )
