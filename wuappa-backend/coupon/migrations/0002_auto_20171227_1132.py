# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='redemption',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='type',
            field=models.CharField(choices=[('MON', 'Fixed amount off'), ('DIS', '% off')], max_length=20),
        ),
    ]
