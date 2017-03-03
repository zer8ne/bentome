# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='meal_order',
        ),
        migrations.AddField(
            model_name='message',
            name='meal',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='home.Meal'),
        ),
    ]