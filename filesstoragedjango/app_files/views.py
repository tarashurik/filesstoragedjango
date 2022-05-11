from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication

from app_files.serializers import FileUploadSerializer
from app_files.models import FileUpload


class FileUploadViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = FileUpload.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)
