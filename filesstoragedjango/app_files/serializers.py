import hashlib

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from filesstoragedjango.settings import MAX_SIZE_MB
from app_files.models import FileUpload


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
        file = validated_data.get('file')
        owner = validated_data.get('owner')

        file_size_mb = file.size / (1024 * 1024)
        if file_size_mb > float(MAX_SIZE_MB):
            raise ValidationError(detail=f"Your file too big - {round(file_size_mb, 2)} MB, please, "
                                         f"upload files less than {MAX_SIZE_MB} MB")

        data = file.file.read()
        file_hash = hashlib.md5(data).hexdigest()
        if FileUpload.objects.filter(owner=owner).filter(file_hash=file_hash):
            raise ValidationError(detail="You have already have File with same content")
        validated_data['file_hash'] = hashlib.md5(data).hexdigest()
        
        return super().create(validated_data)
