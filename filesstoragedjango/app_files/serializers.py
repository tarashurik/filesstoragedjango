import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from filesstoragedjango.settings import MAX_SIZE_MB
from app_files.models import FileUpload


logger = logging.getLogger(__name__)


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = FileUpload
        fields = [
            'id',
            'file',
            'description',
            'owner',
        ]

    def create(self, validated_data):
        logger.info('Start create file')

        file = validated_data.get('file')
        owner = validated_data.get('owner')

        file_size_mb = file.size / (1024 * 1024)
        if file_size_mb > float(MAX_SIZE_MB):
            message = f"Your file too big - {round(file_size_mb, 2)} MB, please, " \
                      f"upload files less than {MAX_SIZE_MB} MB"
            logger.error(msg=message)
            raise ValidationError(detail=message)

        data = file.file.read()
        file_hash = hashlib.md5(data).hexdigest()
        if FileUpload.objects.filter(owner=owner).filter(file_hash=file_hash):
            message = "You have already have File with same content"
            logger.error(msg=message)
            raise ValidationError(detail=message)
        validated_data['file_hash'] = file_hash
        created_file = super().create(validated_data)

        logger.info('End create file')
        return created_file
