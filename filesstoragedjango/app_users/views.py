from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics

from app_users.serializers import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
