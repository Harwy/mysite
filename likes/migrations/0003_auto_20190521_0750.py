# Generated by Django 2.0 on 2019-05-20 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20190508_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likecount',
            options={'verbose_name': '点赞总计', 'verbose_name_plural': '点赞总计'},
        ),
        migrations.AlterModelOptions(
            name='likerecord',
            options={'verbose_name': '单篇点赞数总计', 'verbose_name_plural': '单篇点赞数总计'},
        ),
        migrations.AlterField(
            model_name='likecount',
            name='liked_num',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='likerecord',
            name='like_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='点赞时间'),
        ),
        migrations.AlterField(
            model_name='likerecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='点赞对象'),
        ),
    ]
