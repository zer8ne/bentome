# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_ingredient_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_dish',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
