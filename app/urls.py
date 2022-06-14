from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns=[
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editProfile,name='editprofile'),
    path('accounts/register/',views.register,name='register'),
    path('post/',views.post,name='post'),
    path('accounts/login/',views.loginPage,name='login'),
    path('accounts/logout/',views.logoutUser,name='logout'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("rating/<int:post_id>/", views.rating, name="rating"),
    path("post_view/<int:post_id>/", views.view_post, name="post_view"),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/postview/', views.PostList.as_view()),

]