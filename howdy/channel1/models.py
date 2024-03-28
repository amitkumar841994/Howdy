from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    mobile = models.IntegerField(unique=True,null=False,blank=False)

class UserOtp(models.Model):
    otp=models.IntegerField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)

class Contact(models.Model):
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_name')
    name = models.CharField(max_length=100)
    mobile_no=models.IntegerField(unique=True)


class Message(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
