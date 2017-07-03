from django.contrib import admin

from blog.models import Blog, Post, Subscriptions

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Subscriptions)

