class Restaurant:
    """A class representing a restaurant."""

    # Store two attributes: a restaurant_name and a cuisine_type 
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Method prints name and specialization of the restaurant."""
        print(f"In {self.name} we serve {self.type.title()} cuisine.")

    def open_restaurant(self):
        """Method prints a message that the restaurant is open."""
        print(f"The {self.name} is open now!")

    def set_number_served(self, number):
        """Method sets number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Method increment number of customers who’ve been served."""
        self.number_served += number


restaurant = Restaurant('Rat-a-tat','japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 2
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(5)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(7)
print(f"Number of customers served: {restaurant.number_served}")

