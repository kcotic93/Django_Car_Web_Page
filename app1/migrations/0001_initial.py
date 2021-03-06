# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=50)),
                ('verzija', models.IntegerField()),
                ('godina_proizvodnje', models.DateField(null=True)),
                ('slika', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AutoProizvodjac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('web_stranica', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('logo', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='automodel',
            name='automobili',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.AutoProizvodjac'),
        ),
    ]
