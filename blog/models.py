from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
'''富文本模块引用'''
from ckeditor_uploader.fields import RichTextUploadingField
'''阅读计数模块继承引用'''
from read_statistics.models import ReadNumExpandMethod, ReadDetail




class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name


class Blog(models.Model, ReadNumExpandMethod):  # 继承阅读计数模块下方法：get_read_num，获取当前blog阅读数
    title = models.CharField(max_length=50, verbose_name='标题')
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name='博客类别')
    content = RichTextUploadingField(verbose_name='正文')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='作者')
    read_detail = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        # 排序规则
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = verbose_name
