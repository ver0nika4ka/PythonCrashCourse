class Restaurant:
    """A class representing a restaurant."""

    # Store two attributes: a restaurant_name and a cuisine_type 
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


restaurant = Restaurant('Rat-a-tat','japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()