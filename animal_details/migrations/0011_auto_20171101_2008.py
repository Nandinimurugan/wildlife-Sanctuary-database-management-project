# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-01 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_details', '0010_accounts_organisation_grants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
