from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    blog = models.ForeignKey(Blog)
    creation_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    class Meta:
        unique_together = (("user", "blog"),)

    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.user.username + " " + self.blog.name


class AlreadyReadPost(models.Model):
    class Meta:
        unique_together = (("user", "post"),)

    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.user.username + " " + self.post.name
