# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmissionEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField(unique=True)),
                ('regulated_entity_name', models.CharField(max_length=200)),
                ('physical_location', models.TextField()),
                ('regulated_entity_rn_number', models.CharField(max_length=200)),
                ('city_county', models.CharField(max_length=200)),
                ('type_of_air_emissions_event', models.CharField(max_length=200)),
                ('based_on_the', models.CharField(max_length=200)),
                ('event_began', models.CharField(max_length=200)),
                ('event_ended', models.CharField(max_length=200)),
                ('cause', models.TextField()),
                ('action_taken', models.TextField()),
                ('emissions_estimation_method', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageHTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField(unique=True)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField()),
                ('request_date', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=200)),
                ('status_code', models.CharField(max_length=200)),
                ('failed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
