from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from app_files.serializers import FileUploadSerializer
from app_files.models import FileUpload


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        owner = self.request.user
        serializer.save(owner=owner, file=file)
