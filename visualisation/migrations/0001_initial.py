# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, help_text='If Known')),
                ('month', models.IntegerField(blank=True, help_text='If Known')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MigrationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvalrate', models.DecimalField(decimal_places=15, max_digits=20)),
                ('destination_unemployment', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Destination                                                   Unemployment')),
                ('destination_gdp', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Destination                                          GDP Per Capita')),
                ('destination_rwpvote', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Meaning                                              unknown')),
                ('euplusasyl', models.IntegerField(help_text='Meaning unknown')),
                ('free', models.IntegerField(help_text='Sum of the two Freedom House                               indices of political rights and civil                               liberties, each ranging from 1 (most free)                               to 7 (least free) (AUTOCRACY)')),
                ('genpoliticidemag', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Magnitude score for                                           number of deaths from genocide                                           and politicide (GEN/POLITICIDE)')),
                ('l52dyadasylumcorrpc', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Meaning                                              unknown')),
                ('l52dyadasylumtotalpc', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Meaning                                               unknown')),
                ('origin_gdp', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Origin GDP Per Capita')),
                ('pts', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='average of two Political Terror                              Scales measuring human rights violations,                              ranging from 1 (best) to 5 (worst)')),
                ('recognisedrate', models.DecimalField(decimal_places=15, max_digits=20)),
                ('sfallmax', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Magnitude score for civil                                   war, ethnic war, or collapse of state                                   authority (DOMWAR/STATEFAIL)')),
                ('uppsalaexternalintensity', models.IntegerField(help_text='Intensity of                                                   external conflicts, on an                                                   ordered categorical scale                                                   (0 = no conflict, 1 =                                                   25-999 deaths that year in                                                   minor conflict, 2 = 25-999                                                   deaths that year in                                                   conflict totaling 1000+                                                   deaths across years,                                                   3 = 1000+ deaths that                                                   year)')),
                ('date', models.ForeignKey(help_text='Can input                             just year if full date is unknown', on_delete=django.db.models.deletion.CASCADE, to='visualisation.Date', verbose_name='Date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='visualisation.Country')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='visualisation.Country')),
            ],
        ),
    ]
