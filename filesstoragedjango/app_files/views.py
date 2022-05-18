import logging

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication

from app_files.serializers import FileUploadSerializer
from app_files.models import FileUpload


logger = logging.getLogger(__name__)


class FileUploadViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = FileUpload.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        logger.info('Start creating file')
        owner = self.request.user
        serializer.save(owner=owner)
        logger.info('End creating file')

    def destroy(self, request, *args, **kwargs):
        logger.info('Start deleting file')
        response = super().destroy(request, *args, **kwargs)
        logger.info('End deleting file')
        return response
