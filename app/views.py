from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
# from clone.decorators import unauthenticated_user

# Create your views here.

def index(request):
    posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':posts})


def profile(request):
    return render(request,'pages/profile.html')


def editProfile(request):
    return render(request,'pages/editprofile.html')


def post(request):
        
    return render(request,'pages/addpost.html')

def register(request):
    return render(request,'accounts/register.html')

def loginPage(request):
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')