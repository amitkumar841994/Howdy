from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_name')
    name = models.CharField(max_length=100)
    mobile_no=models.IntegerField(unique=True)






# Create your models here.
