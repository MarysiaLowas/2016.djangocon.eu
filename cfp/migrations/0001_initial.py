# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-06 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('speaker_information', models.TextField(blank=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('audience', models.TextField()),
                ('props', models.TextField(blank=True)),
                ('skill_level', models.PositiveIntegerField(choices=[(1, ''), (2, 'novice'), (3, 'intermediate'), (4, 'advanced')], default=1)),
                ('submitted_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]