# Generated by Django 2.0 on 2019-06-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190612_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userimg',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user_img', verbose_name='头像'),
        ),
    ]