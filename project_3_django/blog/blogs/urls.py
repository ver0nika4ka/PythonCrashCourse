"""Defines URL patterns for blogs.""" 

from django.urls import path
from . import views 

app_name = 'blogs' 

urlpatterns = [  
    # Home page 
    path('', views.index, name='index'),
    # Page shows all the blogposts
    path('blogposts/', views.blogposts, name='blogposts'),
    # Page for all posts of current user
    path('my_blogposts/', views.my_blogposts, name='myposts'),
    # Detailed info about each blogpost
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    # Page for adding a new blogpost
    path('new_post/', views.new_post, name='new_post'),
    # Edit blogpost
    path('edit_post/<int:blogpost_id>/', views.edit_post, name='edit_post'),
    


]
