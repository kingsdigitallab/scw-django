# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 15:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0007_auto_20170321_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorders',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('fips', models.CharField(blank=True, max_length=2, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
                ('iso3', models.CharField(blank=True, max_length=3, null=True)),
                ('un', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('pop2005', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('region', models.SmallIntegerField(blank=True, null=True)),
                ('subregion', models.SmallIntegerField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'tm_world_borders',
                'managed': False,
            },
        ),
    ]
