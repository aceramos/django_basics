# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
