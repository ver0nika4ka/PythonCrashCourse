class User:
    """Class that describes a User"""

    def __init__(self, fname, lname, age, location):
        """Initialize name, last_name, age and location attributes."""
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.location = location

    def describe_user(self):
        """Method printing info about a user."""
        print("Information about user:")
        print(f"\tName: {self.first_name.title()} {self.last_name.title()}")
        print(f"\tAge: {self.age}\n\tLocation: {self.location.title()}")

    def greet_user(self):
        """Method print greeting to user."""
        print(f"Hello, {self.first_name.title()}!\n")