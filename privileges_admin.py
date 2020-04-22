from user import User

class Privileges:
    """Class about privileges for admin and users."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Method shows privileges for Admin user."""
        print(f"Admin user can: {self.privileges}")

class Admin(User):
    """Class for admin with extended privileges."""

    def __init__(self, fname, lname, age, location):
        """Initialize attributes."""
        super().__init__(fname, lname, age, location)
        self.privileges = Privileges()