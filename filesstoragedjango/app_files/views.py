import hashlib

from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from filesstoragedjango.settings import MAX_SIZE_MB
from app_files.serializers import FileUploadSerializer
from app_files.models import FileUpload
from app_files.permissions import IsAuthor


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        owner = self.request.user
        data = file.file.read()
        file_hash = hashlib.md5(data).hexdigest()
        file_size_mb = file.size / (1024*1024)

        if file_size_mb > float(MAX_SIZE_MB):
            raise ValidationError(detail=f"Your file too big - {round(file_size_mb, 2)} MB, please, "
                                         f"upload files less than {MAX_SIZE_MB} MB")
        if FileUpload.objects.filter(owner=self.request.user).filter(file_hash=file_hash):
            raise ValidationError(detail="You have already have File with same content")

        serializer.save(owner=owner, file=file, file_hash=file_hash)

    def list(self, request, *args, **kwargs):
        queryset = FileUpload.objects.filter(owner=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
