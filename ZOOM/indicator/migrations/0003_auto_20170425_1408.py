# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0002_auto_20170421_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatordatapoint',
            name='unit_of_measure',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
