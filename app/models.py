
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    proc_img=CloudinaryField('image',blank=True)
    bio=models.TextField(blank=True,null=True)
    contacts=models.CharField(max_length=200)

    def __str__(self):
        return self.contacts

class Post(models.Model):
    title=models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post_img=CloudinaryField('image',blank=True)
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rate(models.Model):
    title=models.CharField(max_length=100,null=False,blank=True)
    design = models.IntegerField(null=True,default=0)
    usability = models.IntegerField(null=True,default=0)
    content = models.IntegerField(null=True,default=0)
    creativity = models.IntegerField(null=True,default=0)
    total = models.IntegerField(blank=True,null=True,default=0)
    average=models.FloatField(max_length=10,null=True)
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='rate',null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
