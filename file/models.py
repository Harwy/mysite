from django.db import models

# Create your models here.
class FileModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='文件标题')
    file = models.FileField(upload_to="file_center/", verbose_name='文件路径')
    upload_time = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    more = models.TextField(max_length=200, default="...", verbose_name='备注')
