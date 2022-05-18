import logging

from django.contrib.auth.models import User
from rest_framework import permissions, generics

from app_users.serializers import UserSerializer


logger = logging.getLogger(__name__)


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        logger.info("Start creating user")
        response = super().create(request, *args, **kwargs)
        logger.info("End creating user")
        return response
