from datetime import timedelta
from email.policy import default
from time import timezone
import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid

from requests import post
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(
        upload_to='profile_pics', blank=True, default='profile_pics/avatar.png')
    followers = models.ManyToManyField(
        User, related_name='followers', blank=True)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    story = models.ManyToManyField(
        'Story', related_name='story', blank=True)

    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.user.username)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.body)

class Story(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='story_woner')
    image = models.ImageField(upload_to='story_pics', blank=True, default='story_pics/avatar.png')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.image)

class Post(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics')
    caption = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    likes = models.ManyToManyField(
        Profile, related_name='Likes', blank=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name='comments')
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.caption)
    
class Notification(models.Model):
    user_to_notify = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_to_notify')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_notification')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.user)


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")

#if the user is deleted then the profile is also deleted
@receiver(post_delete, sender=Profile)
def delete_user_profile(sender, instance, **kwargs):
    instance.user.delete()
    print("Profile deleted")

#everytime a user follows another user, a notification is created

#everytime a user likes a post, a notification is created
        