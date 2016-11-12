# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-11 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0002_building_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaundryMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('status', models.SmallIntegerField(choices=[(1, 'OCCUPIED'), (0, 'AVAILABLE')])),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Building')),
            ],
        ),
        migrations.CreateModel(
            name='StatusChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_status', models.SmallIntegerField(choices=[(1, 'OCCUPIED'), (0, 'AVAILABLE')])),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.LaundryMachine')),
            ],
        ),
    ]
