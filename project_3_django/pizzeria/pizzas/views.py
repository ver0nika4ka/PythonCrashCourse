from django.shortcuts import render
from .models import Pizza, Topping 

# Create your views here.
def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas from database."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    # Building page with data, pass request object and the path to the template and pass the context variable to render().
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show toppings for current pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)

def toppings(request):
    """Show all available toppings."""
    toppings = Topping.objects.all()
    context = {'toppings':toppings}
    return render(request, 'pizzas/toppings.html', context)

