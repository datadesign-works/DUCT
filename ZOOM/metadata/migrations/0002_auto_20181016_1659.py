# Generated by Django 2.1.2 on 2018-10-16 16:59

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='mapping_used',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
