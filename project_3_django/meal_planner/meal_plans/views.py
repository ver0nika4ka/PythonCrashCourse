from django.shortcuts import render, redirect
from .models import MealPost

# Create your views here.
def index(request):
    """The home page for Meal Planner."""
    return render(request, 'index.html')

def meals_posts(request):
    """Show all meal posts."""
    meals_posts = MealPost.objects.order_by('date_added')
    context = {'meals_posts': meals_posts}
    return render(request, 'meals_posts.html', context)

def meal_post(request, meal_post_id):
    """Show current meal post."""
    meal_post =MealPost.objects.get(id=meal_post_id)
    context = {'meal_post': meal_post}
    return render(request, 'meal_post.html', context)
