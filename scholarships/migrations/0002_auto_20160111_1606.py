# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2016-01-11 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='financial_assistance',
            field=models.CharField(max_length=150),
        ),
    ]
