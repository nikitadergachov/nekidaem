# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 19:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_auto_20170703_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog', verbose_name='Блог')),
                ('readed', models.ManyToManyField(related_name='_subscribe_readed_+', to='blogs.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Подписанный пользователь')),
            ],
            options={
                'verbose_name': 'Подписки',
                'verbose_name_plural': 'Подписка',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='readed',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([('user', 'blog')]),
        ),
    ]