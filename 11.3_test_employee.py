import unittest
from Employee_11_3 import Employee

class TestSalaryRaise(unittest.TestCase):
    """Tests for the class TestSalaryRaise."""
    def setUp(self):
        """Create an employee."""
        self.employee = Employee('Veronica','Ivanova', 30_000)

    def test_give_default_raise(self):
        """Testing salary raise by default."""
        # Create an instance of Employee
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 35_000)

    def test_give_custom_raise(self):
        """Testing salary raise by different amount."""
        self.employee.give_raise(7_000)
        self.assertEqual(self.employee.salary, 37_000)


if __name__ == '__main__':
    unittest.main()