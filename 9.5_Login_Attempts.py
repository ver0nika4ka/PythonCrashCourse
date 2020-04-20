class User:
    """Class that describes a User"""
    def __init__(self, fname, lname, age, location):
        """Initialize name, last_name, age and location attributes."""
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Method printing info about a user."""
        print("Information about user:")
        print(f"\tName: {self.first_name.title()} {self.last_name.title()}")
        print(f"\tAge: {self.age}\n\tLocation: {self.location.title()}")

    def greet_user(self):
        """Method print greeting to user."""
        print(f"Hello, {self.first_name.title()}!\n")

    def increment_login_attempts(self):
        """Method increments the value of login_attempts by 1."""
        self.login_attempts += 1 

    def reset_login_attempts(self):
        """Method resets the value of login_attempts to 0."""
        self.login_attempts = 0

user_1 = User('veronica','ivanova','20','belarus')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)


        