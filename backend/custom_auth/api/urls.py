from django.urls import include, path

from custom_auth.api.views import LoginView, TwoFactorAuthView

app_name = 'custom_auth'

auth_urlpatterns = [
    path(
        'login/', LoginView.as_view(), name='login'
    ),
    path('login/2fa/', TwoFactorAuthView.as_view(), name='2fa'),
    path('', include('djoser.urls')),
]
