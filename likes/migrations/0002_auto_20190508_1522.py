# Generated by Django 2.0 on 2019-05-08 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecount',
            old_name='like_num',
            new_name='liked_num',
        ),
    ]
