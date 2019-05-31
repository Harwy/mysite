# Generated by Django 2.0 on 2019-05-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190508_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time'], 'verbose_name': '评论库', 'verbose_name_plural': '评论库'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='提交评论时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='评论内容'),
        ),
    ]
