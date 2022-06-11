from django import forms
from .models import *
from django.forms import ModelForm




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','proc_img','bio','email','contacts']