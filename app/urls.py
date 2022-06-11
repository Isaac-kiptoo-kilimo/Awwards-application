from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editProfile,name='editprofile'),
    path('accounts/register/',views.register,name='register'),
    path('post/',views.post,name='post'),
    path('accounts/login/',views.loginPage,name='login'),
    path('accounts/logout/',views.logoutUser,name='logout'),
]