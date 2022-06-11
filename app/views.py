from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# from clone.decorators import unauthenticated_user
from .forms import ProfileForm


def index(request):
    user_posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':user_posts})


def profile(request):
    user=User.objects.all()
    return render(request,'pages/profile.html',{'users':user})


def editProfile(request):
    profiles= Profile.objects.get(user=request.user)
   
    if request.method == 'POST':
       
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            
            prof_form.save()
            return redirect('profile')
            
            
    else:
        # user_form = UpdateUserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
             
    context={
        # 'user_form': user_form,
        'prof_form': prof_form,
        'profiles': profiles
          
        }
    return render(request,'pages/editprofile.html',context)


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
    if request.method=='POST':
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:   
            new_user,create = User.objects.get_or_create(username=username)
            if create:
                try:
                    validate_password(password1)
                    new_user.set_password(password1)
                    new_user.profile.first_name=first_name
                    new_user.profile.last_name=last_name
                    new_user.profile.username=username
                    new_user.profile.email=email
                    new_user.profile.save()
                    new_user.save()
                    return redirect('login')
                except ValidationError as e:
                    messages.error(request,'Password error {e} ')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register')    

    return render(request,'accounts/register.html')


def loginPage(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
       
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')