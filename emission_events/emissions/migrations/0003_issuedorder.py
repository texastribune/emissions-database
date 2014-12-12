# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0002_auto_20141105_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docket_number', models.CharField(max_length=20, unique=True, null=True)),
                ('agenda_date', models.CharField(max_length=20, null=True)),
                ('penalty_amount', models.CharField(max_length=30, null=True)),
                ('summary', models.CharField(max_length=1000, null=True)),
                ('regulated_entity_rn_number', models.CharField(max_length=50)),
                ('docket_link', models.CharField(max_length=200, null=True)),
                ('commission_issued_order', models.CharField(max_length=200, null=True)),
                ('agended_at', models.DateField(null=True, db_index=True)),
                ('penalty_value', models.IntegerField(null=True)),
                ('regulated_entity', models.ForeignKey(to='emissions.RegulatedEntity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
