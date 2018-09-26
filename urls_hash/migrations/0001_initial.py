# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-25 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_value', models.CharField(max_length=15, unique=True)),
                ('url', models.URLField()),
            ],
        ),
    ]
