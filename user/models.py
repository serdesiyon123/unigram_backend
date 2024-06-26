from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


user_model = settings.AUTH_USER_MODEL

class User(AbstractUser):
    email = models.EmailField(unique = True, blank = False)
    first_name = models.CharField(max_length=255,blank = False)
    last_name = models.CharField(max_length=255,blank = False)

    REQUIRED_FIELDS = ['first_name','last_name','email',]


class Profile(models.Model):
    user = models.OneToOneField(user_model,on_delete = models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='user/profile',blank=True)
    bio = models.TextField(null=True,blank=True)
    org_email = models.EmailField(blank=True)
    verified_org = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s profile"


class Badge(models.Model):
    badge_name = models.CharField(max_length=200)
    badge_image = models.ImageField(upload_to='user/badge')
    badge_description = models.TextField(max_length=500)

    def __str__(self):
        return self.badge_name

class UserBadge(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return f"{self.user.user.username}'s {self.badge.badge_name} badge"


class Point(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='points')
    value = models.IntegerField()
    reason = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.value} points - {self.reason}"
    

class Notification(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    sender_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_notifications', null=True)
    following = models.BooleanField(default=False)
    answer = models.ForeignKey('post.Comment', on_delete=models.CASCADE, related_name='answer_notifications', null=True)

    def __str__(self):
        return self.message


