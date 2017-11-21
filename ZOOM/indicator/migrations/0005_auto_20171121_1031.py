# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 10:31
from __future__ import unicode_literals

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0004_auto_20170609_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatordatapoint',
            name='search_vector_text',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='indicatordatapoint',
            index=django.contrib.postgres.indexes.GinIndex(fields=[b'search_vector_text'], name='indicator_i_search__28779d_gin'),
        ),
    ]
