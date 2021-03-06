# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20170715_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='current_salary',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='years_in_workplace',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
