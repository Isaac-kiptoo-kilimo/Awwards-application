from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
# from clone.decorators import unauthenticated_user

# Create your views here.

def index(request):
    user_posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':user_posts})


def profile(request):
    return render(request,'pages/profile.html')


def editProfile(request):
    return render(request,'pages/editprofile.html')


def post(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        title=request.POST.get('title')
        description=request.POST.get('description')
        posts=Post(post_img=photo,title=title,description=description)
        posts.save_post()
        print('new post is ',posts)
        return redirect('index')
    return render(request,'pages/addpost.html')

def register(request):
    return render(request,'accounts/register.html')

def loginPage(request):
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')