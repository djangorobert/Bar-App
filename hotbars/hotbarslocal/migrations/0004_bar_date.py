# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotbarslocal', '0003_remove_bar_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]