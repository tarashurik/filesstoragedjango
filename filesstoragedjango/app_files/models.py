from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, verbose_name='ID')
    file = models.FileField(upload_to=f'files/', verbose_name='File')
    description = models.TextField(blank=True, verbose_name='Description')

    owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, verbose_name='Owner')

    class Meta:
        db_table = 'files'
