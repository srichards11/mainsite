# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0002_userdata_is_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='subscribed_email',
            field=models.BooleanField(default=False),
        ),
    ]