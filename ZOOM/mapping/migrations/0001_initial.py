# Generated by Django 2.1.2 on 2018-10-31 21:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('file_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.FileSource')),
            ],
        ),
    ]
