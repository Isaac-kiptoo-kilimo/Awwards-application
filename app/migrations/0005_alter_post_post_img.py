# Generated by Django 4.0.5 on 2022-06-11 07:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='post_img'),
        ),
    ]
