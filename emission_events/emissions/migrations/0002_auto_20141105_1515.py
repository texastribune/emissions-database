# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegulatedEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('regulated_entity_rn_number', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('primary_business', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=30)),
                ('nearest_city', models.CharField(max_length=30)),
                ('nearest_zipcode', models.CharField(max_length=30)),
                ('physical_location', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='REPermit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program', models.CharField(max_length=200, null=True)),
                ('id_type', models.CharField(max_length=200, null=True)),
                ('id_number', models.CharField(max_length=200, null=True)),
                ('id_status', models.CharField(max_length=200, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('proposed_enforcement_orders', models.BooleanField(default=False)),
                ('effective_enforcement_orders', models.BooleanField(default=False)),
                ('notice_of_violations', models.BooleanField(default=False)),
                ('regulated_entity', models.ForeignKey(to='emissions.RegulatedEntity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='emissionevent',
            name='regulated_entity',
            field=models.ForeignKey(default=None, to='emissions.RegulatedEntity', null=True),
            preserve_default=True,
        ),
    ]
