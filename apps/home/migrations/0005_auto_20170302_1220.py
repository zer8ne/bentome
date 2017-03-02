# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170302_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='side_dish',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='side_dish',
            name='meal',
            field=models.ManyToManyField(blank=True, related_name='side_dishes', to='home.Meal'),
        ),
    ]
