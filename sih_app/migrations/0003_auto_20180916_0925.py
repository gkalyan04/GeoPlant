# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-16 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0002_auto_20180916_0923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plants',
            new_name='Plant',
        ),
    ]