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


class Admin(User):
    """Class for admin with extended privileges."""

    def __init__(self, fname, lname, age, location):
        """Initialize attributes."""
        super().__init__(fname, lname, age, location)
        self.privileges = Privileges()


class Privileges:
    """Class about privileges for admin and users."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Method shows privileges for Admin user."""
        print(f"Admin user can: {self.privileges}")

# Created an instance of Admin and then called method show_privileges()
admin_user = Admin('veronica','ivanova','20','belarus')
admin_user.privileges.show_privileges()
