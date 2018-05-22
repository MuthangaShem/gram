# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0013_remove_image_image_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, upload_to='avatars'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]