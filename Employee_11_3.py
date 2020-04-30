class Employee:
    """Store info about employee."""

    def __init__(self, f_name, l_name, salary):
        """Store name, surname and annual salary."""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, raise_amount=5_000):
        """Raise a salary by raise amount."""
        self.salary += raise_amount
