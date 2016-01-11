# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2016-01-11 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('why', models.TextField()),
                ('financial_assistance', models.TextField()),
                ('location', models.TextField()),
                ('submitted_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
