# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-28 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_models', '0002_auto_20190524_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbhttpinterface',
            name='uslRedirect',
            field=models.IntegerField(db_column='uslRedirect', default=1, verbose_name='是否自动重定向'),
        ),
        migrations.AddField(
            model_name='tbhttptestcasestep',
            name='uslRedirect',
            field=models.IntegerField(db_column='uslRedirect', default=1, verbose_name='是否自动重定向'),
        ),
    ]
