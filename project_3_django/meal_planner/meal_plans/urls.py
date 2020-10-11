from django.urls import path
from . import views 

app_name = 'meal_plans' 
urlpatterns = [ 
    # Home page 
    path('', views.index, name='index'), 
    path('meal_plans/', views.meals_posts, name='meals_posts'),
    path('meal_plans/<int:meal_post_id>/',views.meal_post, name='meal_post'),

]