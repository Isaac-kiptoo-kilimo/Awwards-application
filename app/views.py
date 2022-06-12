from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def index(request):
    user_posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':user_posts})

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
        posts=Post(post_img=photo,title=title,url=url,technologies=technologies,description=description)
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





# def project(request, post_id):
#     post = Post.objects.get(id=post_id)
#     ratings = Rate.objects.filter(user=request.user, id=post_id).first()
#     rating_status = None
#     if ratings is None:
#         rating_status = False
#     else:
#         rating_status = True
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.user = request.user
#             rate.post = post
#             rate.save()
#             post_ratings = Rate.objects.filter(post=post)

#             design_ratings = [d.design for d in post_ratings]
#             design_average = sum(design_ratings) / len(design_ratings)

#             usability_ratings = [us.usability for us in post_ratings]
#             usability_average = sum(usability_ratings) / len(usability_ratings)

#             content_ratings = [content.content for content in post_ratings]
#             content_average = sum(content_ratings) / len(content_ratings)

#             score = (design_average + usability_average + content_average) / 3
#             print(score)
#             rate.design_average = round(design_average, 2)
#             rate.usability_average = round(usability_average, 2)
#             rate.content_average = round(content_average, 2)
#             rate.score = round(score, 2)
#             rate.save()
#             print('scrore 2',score)
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = RateForm()
#     params = {
#         'post': post,
#         'rating_form': form,
#         'rating_status': rating_status

#     }
#     return render(request, 'pages/project.html', params)


def rating(request, title):
    if request.method =="POST":
        project = Post.objects.get(title=title),
        # user = request.user,
        comment = request.POST['comment']
        design= request.POST['design']
        usability= request.POST['usability']
        content= request.POST['content']
        creativity= request.POST['creativity']
          
        ratings = Rate.objects.create(
            # project = project,
            # user = user,
            comment = comment,
            design=design,
            usability=usability,
            content=content, 
            creativity=creativity,
            total= (int(design)) + (int(usability)) + (int(content)) + (int(creativity)) ,    
        )
        ratings.save()
        # print(ratings)
        # average_creativity= sum(creativity)/len(creativity) 
        # average_design= sum(design)/len(design) 
        # average_usability= sum(usability)/len(usability)
        # average_content= sum(content)/len(content)
        # average =(average_creativity+ average_content+ average_design + average_usability)/4
        
        return redirect ('index')
    return render(request, 'pages/rating.html')

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