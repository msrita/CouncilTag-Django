# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('injest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendarecommendation',
            old_name='agenda',
            new_name='agenda_item',
        ),
    ]
