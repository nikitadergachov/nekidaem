# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 07:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20170704_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
