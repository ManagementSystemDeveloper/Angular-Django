# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import djmoney.models.fields
import languages.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20180124_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='language',
            field=languages.fields.LanguageField(choices=[('en', 'English')], max_length=3),
        ),
        migrations.AlterField(
            model_name='hireservice',
            name='review_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='hireservice',
            name='total_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro'), ('CHF', 'Swiss Franc')], default='CHF', editable=False, max_length=3),
        ),
    ]
