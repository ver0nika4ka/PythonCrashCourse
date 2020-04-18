class Restaurant:
    """A class representing a restaurant."""

    # Store two attributes: a restaurant_name and a cuisine_type 
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Method prints name and specialization of the restaurant."""
        print(f"In {self.name.title()} we serve {self.type.title()} cuisine.")

    def open_restaurant(self):
        """Method prints a message that the restaurant is open."""
        print(f"The {self.name.title()} is open now!")

# Strait solution
# restaurant1 = Restaurant('rat-a-tat','japanese')
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()

# restaurant2 = Restaurant('minsk','belarusian')
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()

# restaurant3 = Restaurant('pelmeshka','russian')
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()

# restaurant4 = Restaurant('kappa','japanese')
# restaurant4.describe_restaurant()
# restaurant4.open_restaurant()

# Solution with list of tuples
restaurants_info = [('rat-a-tat','japanese'), ('minsk','belarusian'), 
                    ('pelmeshka','russian'), ('kappa','japanese')]
for name, cuisine in restaurants_info:
    restaurant = Restaurant(name, cuisine)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

# for rest_info in restaurants_info:
#     name, cuisine = rest_info
#     restaurant = Restaurant(name, cuisine)
#     restaurant.describe_restaurant()
#     restaurant.open_restaurant()