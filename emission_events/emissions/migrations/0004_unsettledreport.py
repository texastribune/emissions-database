# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0003_issuedorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnsettledReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_number', models.IntegerField(unique=True)),
            ],
        ),
    ]
