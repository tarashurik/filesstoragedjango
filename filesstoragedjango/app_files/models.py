from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return f'{instance.owner.id}/{filename}'


class FileUpload(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, verbose_name='ID')
    file = models.FileField(upload_to=user_directory_path, verbose_name='File')
    file_hash = models.CharField(max_length=255, null=False, verbose_name='File hash', auto_created=True)
    description = models.TextField(blank=True, verbose_name='Description')

    owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, verbose_name='Owner')

    class Meta:
        db_table = 'files'
