# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170228_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_4_digits',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
