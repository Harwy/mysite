from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


'''点赞总数'''
class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    liked_num = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        verbose_name = '点赞总计'
        verbose_name_plural = verbose_name


'''点赞具体'''
class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='点赞对象')  # 点赞人
    like_time = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')  # 点赞时间

    class Meta:
        verbose_name = '单篇点赞数总计'
        verbose_name_plural = verbose_name