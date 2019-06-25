from django.contrib import admin
from .models import FileModel

# Register your models here.
@admin.register(FileModel)
class FileModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_time')