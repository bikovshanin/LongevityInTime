import shortuuid
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core.tesks import delete_expired_2fa_code, send_confirmation_email
from custom_auth.api.serializers import LoginSerializer, TokenSerializer
from users.models import User


class LoginView(generics.CreateAPIView):
    """
    Validates login credentials and sends confirmation code.
    """
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = authenticate(
                email=email,
                password=serializer.validated_data['password']
            )
            user.confirmation_code = shortuuid.uuid()[:6]
            user.save()
            send_confirmation_email.delay(user.email, user.confirmation_code)
            delete_expired_2fa_code.apply_async((user.id,), countdown=300)
            return Response(
                {
                    'email': email,
                    'detail': 'Confirmation code has been sent to your email'
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class TwoFactorAuthView(generics.CreateAPIView):
    """
    Validates confirmation code and issues JWT token.
    """
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=request.data.get('email'))
        except User.DoesNotExist:
            return Response(
                {'email': 'Not Found'},
                status=status.HTTP_404_NOT_FOUND
            )
        if request.data.get('confirmation_code') == user.confirmation_code:
            user.confirmation_code = ''
            user.save()
            token = RefreshToken.for_user(user).access_token
            return Response({'token': str(token)},
                            status=status.HTTP_201_CREATED)
        return Response({'confirmation_code': 'Invalid Code'},
                        status=status.HTTP_400_BAD_REQUEST)
