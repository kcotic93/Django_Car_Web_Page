# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automodel',
            name='slika',
            field=models.CharField(max_length=300),
        ),
    ]
