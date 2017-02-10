# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0006_auto_20170206_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieptank',
            name='multiplier',
        ),
        migrations.AddField(
            model_name='dieptank',
            name='opness',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tier 1'), (2, 'Tier 2'), (3, 'Tier 3')], default=1),
        ),
    ]
