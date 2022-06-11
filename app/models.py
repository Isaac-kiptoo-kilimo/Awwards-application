
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
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    proc_img=CloudinaryField('image',blank=True)
    bio=models.TextField(blank=True,null=True)
    contacts=models.CharField(max_length=200)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

  

    def update_profile(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


class Post(models.Model):
    title=models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    post_img=CloudinaryField('post_img')
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

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

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    def update_rate(self):
        self.update()
        
    def __str__(self):
        return self.title
