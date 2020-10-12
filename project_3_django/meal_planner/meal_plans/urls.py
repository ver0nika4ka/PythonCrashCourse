from django.urls import path
from . import views 

app_name = 'meal_plans' 
urlpatterns = [ 
    # Home page 
    path('', views.index, name='index'), 
    path('meals_posts/', views.meals_posts, name='meals_posts'),
    path('meals_posts/<int:meal_post_id>/',views.meal_post, name='meal_post'),

]