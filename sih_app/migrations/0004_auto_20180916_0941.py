# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-16 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0003_auto_20180916_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='first_name',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='last_name',
            new_name='plant_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='email',
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_breed',
            field=models.CharField(default='', max_length=264),
            preserve_default=False,
        ),
    ]
