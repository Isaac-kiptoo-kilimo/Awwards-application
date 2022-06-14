
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.decorators import unauthenticated_user
from .models import *
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# from clone.decorators import unauthenticated_user
from .forms import ProfileForm,RateForm
from django.db.models import Q 
from django.views.generic import TemplateView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer,ProfileSerializer
from datetime import date

@login_required(login_url='login')
def index(request):
    today = date.today()
    user_posts=Post.objects.all()
    post=Post.objects.all().first()
    ratings=Rate.objects.filter(post=post)
    aves=create_average(ratings)
    
    return render(request,'pages/index.html',{'posts':user_posts,'today':today,'post':post,'aves':aves})

@login_required(login_url='login')
def profile(request):
    user=User.objects.all()
    return render(request,'pages/profile.html',{'users':user})

@login_required(login_url='login')
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

@login_required(login_url='login')
def post(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        title=request.POST.get('title')
        url=request.POST.get('url')
        technologies=request.POST.get('technologies')
        description=request.POST.get('description')
        posts=Post(post_img=photo,title=title,url=url,technologies=technologies,description=description,user=request.user)
        posts.save_post()
        print('new post is ',posts)
        return redirect('index')
    return render(request,'pages/addpost.html')

def view_post(request,post_id):
    post = Post.objects.get(id=post_id)
    cxt={
        'post':post
    }
    return render(request,'pages/view_post.html',cxt)

@unauthenticated_user
def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:   
            new_user,create = User.objects.get_or_create(username=username,email=email)
            if create:
                try:
                    validate_password(password1)
                    new_user.set_password(password1)
                    new_user.profile.fullname=fullname
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

@unauthenticated_user
def loginPage(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
       
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('index')


class SearchResultsView(ListView):
    model = Post
    template_name = "pages/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = Post.objects.filter(
            Q(title__icontains=query)
        )
        return object_list




@login_required(login_url='login')
def rating(request,post_id):

    user=request.user
    post=Post.objects.get(id=post_id)
    ratings=Rate.objects.filter(post=post)
    
    form=RateForm(request.POST)
    if request.method=='POST':
       if form.is_valid():
           design=form.cleaned_data['design']
           usability=form.cleaned_data['usability']
           content=form.cleaned_data['content']
           creativity=form.cleaned_data['creativity']
           new_rate=Rate(design=design,usability=usability,content=content,creativity=creativity,user=user,post=post)
           new_rate.save()
           return redirect('rating',post_id=post_id)
    cxt={
        'form':form,
        'post':post,
        'ratings':create_average(ratings)
    }
    return render(request,'pages/rating.html',cxt)

def create_average(ratings):
    design=0
    usability=0
    content=0
    creativity=0
    for rate in ratings:
        design+=int(rate.design)
        usability+=int(rate.usability)
        content+=int(rate.content)
        creativity+=int(rate.creativity)
    
    des_av=design/len(ratings)
    usa_av=usability/len(ratings)
    con_av=content/len(ratings)
    creat_av=creativity/len(ratings)
    score_av=(des_av+usa_av+con_av+creat_av)/4
    return {
        'design_average':des_av,
        'usability_average':usa_av,
        'content_average':con_av,
        'creativity_average':creat_av,
        'score_average':score_av
    }

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers =  ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers =  PostSerializer(all_post, many=True)
        return Response(serializers.data)

