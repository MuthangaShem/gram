# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20180514_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_avatar',
            new_name='avatar_thumbnail',
        ),
    ]
