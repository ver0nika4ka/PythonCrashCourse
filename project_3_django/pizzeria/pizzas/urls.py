"""Defines URL patterns for pizzas."""
from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all avaliable pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detailed page that shows chosen pizza's toppings.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    # Page with all availablle toppings.
    path('toppings/', views.toppings, name='toppings'),

]