# Generated by Django 2.1.2 on 2018-12-03 07:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
