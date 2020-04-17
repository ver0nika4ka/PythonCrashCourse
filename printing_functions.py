def make_sandwich(*toppings):
    print(toppings)

def car_info(manufacturer, model, **kwargs):
    kwargs['manufacturer_name'] = manufacturer
    kwargs['model_name'] = model
    return kwargs

def make_pizza(size, *toppings):
       """Summarize the pizza we are about to make."""
       print(f"\nMaking a {size}-inch pizza with the following toppings:")
       for topping in toppings:
           print(f"- {topping}")