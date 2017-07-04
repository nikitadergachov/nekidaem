from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=100, verbose_name='Название блога')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок поста')
    content = models.TextField(max_length=2000, verbose_name='Контент поста')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Блог')
    creation_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Subscribe(models.Model):
    class Meta:
        unique_together = (("user", "blog"),)
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписка'

    user = models.ForeignKey(User ,on_delete=models.CASCADE, verbose_name='Подписанный пользователь', related_name='subscribe')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Блог', related_name='subscribe')
    readed = models.ManyToManyField(Post, related_name='+')

    def __str__(self):
        return self.user.username + " " + self.blog.name



