from django.contrib import admin
from .models import Profile, Post, Comment, Story, Notification, Email
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Story)
admin.site.register(Notification)
admin.site.register(Email)