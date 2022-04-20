from rest_framework import serializers

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
