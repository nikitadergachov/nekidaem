# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 18:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Подписки',
                'verbose_name_plural': 'Подписка',
            },
        ),
        migrations.AlterUniqueTogether(
            name='alreadyreadpost',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='alreadyreadpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='alreadyreadpost',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='subscriptions',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название блога'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog', verbose_name='Блог'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2000, verbose_name='Контент поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Заголовок поста'),
        ),
        migrations.DeleteModel(
            name='AlreadyReadPost',
        ),
        migrations.DeleteModel(
            name='Subscriptions',
        ),
        migrations.AddField(
            model_name='subscription',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog', verbose_name='Блог'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='readed',
            field=models.ManyToManyField(related_name='_subscription_readed_+', to='blogs.Post'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Подписанный пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'blog')]),
        ),
    ]