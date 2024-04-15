from django.urls import include, path

app_name = 'users'

users_urlpatterns = [
    path('', include('djoser.urls')),
]
