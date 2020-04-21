class Restaurant:
    """A class representing a restaurant."""

    #Store two attributes: a restaurant_name and a cuisine_type 
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Method prints name and specialization of the restaurant."""
        print(f"In {self.name} we serve {self.type.title()} cuisine.")

    def open_restaurant(self):
        """Method prints a message that the restaurant is open."""
        print(f"The {self.name} is open now!")

class IceCreamStand(Restaurant):
    """Represent a different ice-cream"""

    def __init__(self, name, r_type, flavors):
        """Initialize attributes of the parent class Restaurant."""
        super().__init__(name, r_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Flavors of ice-cream that we have: {self.flavors}")


restaurant = Restaurant('Rat-a-tat','japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

flvrs = ['vanila', 'strawberry']

ice_cream_shop = IceCreamStand('Morozhko','ice-cream', flvrs)
ice_cream_shop.describe_restaurant()
ice_cream_shop.open_restaurant()
ice_cream_shop.display_flavors()
