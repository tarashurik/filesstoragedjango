from django.contrib import admin

from app_files.models import FileUpload


@admin.register(FileUpload)
class FileAdmin(admin.ModelAdmin):
    pass
