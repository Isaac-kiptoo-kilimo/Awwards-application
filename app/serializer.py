from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email', 'proc_img', 'bio')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','user','post_img','url','technologies', 'description', 'created_at')