# Generated by Django 2.0 on 2019-05-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190521_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_cover',
            field=models.ImageField(blank=True, default='blog_img/default.png', height_field=75, null=True, upload_to='blog_img/%Y/%m/%d', verbose_name='博客封面', width_field=75),
        ),
    ]
