# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContaminantReleased',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField()),
                ('contaminant', models.CharField(max_length=100)),
                ('authorization', models.CharField(max_length=200)),
                ('limit', models.CharField(max_length=100)),
                ('amount_released', models.CharField(max_length=200)),
                ('contaminant_parameterized', models.CharField(max_length=100, db_index=True)),
                ('limit_lbs', models.FloatField(null=True)),
                ('amount_released_lbs', models.FloatField(null=True)),
                ('limit_op', models.FloatField(null=True)),
                ('amount_released_op', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmissionEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField(unique=True)),
                ('dc_date_meta', models.CharField(max_length=20, null=True)),
                ('regulated_entity_name', models.CharField(max_length=30)),
                ('physical_location', models.TextField()),
                ('regulated_entity_rn_number', models.CharField(max_length=50)),
                ('city_county', models.CharField(max_length=50)),
                ('type_of_air_emissions_event', models.CharField(max_length=200)),
                ('based_on_the', models.CharField(max_length=50)),
                ('event_began', models.CharField(max_length=30)),
                ('event_ended', models.CharField(max_length=30)),
                ('cause', models.TextField()),
                ('action_taken', models.TextField()),
                ('emissions_estimation_method', models.TextField()),
                ('dc_date', models.DateField(null=True)),
                ('city', models.CharField(max_length=200, null=True, db_index=True)),
                ('county', models.CharField(max_length=200, null=True, db_index=True)),
                ('began_date', models.DateTimeField(null=True, db_index=True)),
                ('ended_date', models.DateTimeField(null=True, db_index=True)),
                ('duration', models.FloatField(null=True)),
                ('type_of_emission', models.CharField(max_length=30, db_index=True)),
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
        migrations.AddField(
            model_name='emissionevent',
            name='page_html',
            field=models.ForeignKey(to='emissions.PageHTML'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contaminantreleased',
            name='emission_event',
            field=models.ForeignKey(to='emissions.EmissionEvent'),
            preserve_default=True,
        ),
    ]
