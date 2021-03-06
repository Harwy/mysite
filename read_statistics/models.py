from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone

'''
阅读计数基础模块
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0, verbose_name='阅读数')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '总阅读计数库'
        verbose_name_plural = verbose_name


'''
阅读计数模块基础方法——用于继承
用法：class obj(models.Model, ReadNumExpandMethod)
功能：对应model下添加get_read_num方法，用于返回该model阅读数
'''
class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0, verbose_name='阅读数')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '单篇阅读计数库'
        verbose_name_plural = verbose_name
