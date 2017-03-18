# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-16 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20161231_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripesubscription',
            name='plan',
            field=models.CharField(blank=True, choices=[('family_monthly', 'Family Monthly Subscription'), ('family_yearly', 'Family Yearly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('basic_monthly', 'Basic Monthly Subscription'), ('basic_yearly', 'Basic Yearly Subscription')], max_length=255, null=True),
        ),
    ]