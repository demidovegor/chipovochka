# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModelName', models.TextField()),
                ('info_v', models.TextField()),
                ('info_type_ebu', models.TextField()),
                ('info_price', models.TextField()),
                ('BrandName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.car_brand')),
            ],
        ),
    ]
