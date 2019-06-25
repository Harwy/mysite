# Generated by Django 2.0 on 2019-05-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190531_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='profile',
            name='userimg',
            field=models.ImageField(blank=True, default='avatar\\default_64.png', null=True, upload_to='user_img/%Y/%m/%d', verbose_name='头像'),
        ),
    ]
