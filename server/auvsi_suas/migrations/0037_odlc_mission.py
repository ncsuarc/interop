# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-10 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auvsi_suas', '0036_takeofforlandingevent_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='odlc',
            name='mission',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='auvsi_suas.MissionConfig'),
            preserve_default=False, ),
    ]
