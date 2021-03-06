# Generated by Django 2.1.2 on 2018-11-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_initial'),
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoints',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('date', models.CharField(max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateFormat',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilterHeadings',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('aggregation_allowed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('datapoints', models.ManyToManyField(related_name='filters', to='indicator.Datapoints')),
                ('date_format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.DateFormat')),
                ('geolocations', models.ManyToManyField(to='geodata.Geolocation')),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.FilterHeadings')),
                ('metadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.File')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('file_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.FileSource')),
            ],
        ),
        migrations.CreateModel(
            name='ValueFormat',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='filters',
            name='value_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.ValueFormat'),
        ),
        migrations.AddField(
            model_name='filterheadings',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.Indicator'),
        ),
        migrations.AddField(
            model_name='datapoints',
            name='date_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.DateFormat'),
        ),
        migrations.AddField(
            model_name='datapoints',
            name='geolocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodata.Geolocation'),
        ),
        migrations.AddField(
            model_name='datapoints',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.Indicator'),
        ),
        migrations.AddField(
            model_name='datapoints',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.File'),
        ),
        migrations.AddField(
            model_name='datapoints',
            name='value_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.ValueFormat'),
        ),
    ]
