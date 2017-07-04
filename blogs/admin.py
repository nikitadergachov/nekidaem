from django.contrib import admin

from blogs.models import Blog, Post, Subscribe

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Subscribe)

