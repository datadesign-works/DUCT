# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-24 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0005_auto_20170124_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicatordatapoint',
            old_name='indicator_category',
            new_name='indicator_category_id',
        ),
    ]