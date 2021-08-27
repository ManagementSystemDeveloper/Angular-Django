# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0011_auto_20170808_0628'),
        ('services', '0011_auto_20171213_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireservice',
            name='charges',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Charge'),
        ),
    ]