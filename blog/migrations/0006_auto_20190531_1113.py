# Generated by Django 2.0 on 2019-05-31 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190521_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_cover',
            field=models.ImageField(blank=True, default='blog_img/default.png', null=True, upload_to='blog_img/%Y/%m/%d', verbose_name='博客封面'),
        ),
    ]
