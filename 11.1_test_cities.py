import unittest
from city_functions_11_1 import get_city_country

class NamesTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country_name(self):
        """Do Tokyo, Japan works?"""
        full_name = get_city_country('tokyo', 'japan')
        self.assertEqual(full_name, 'Tokyo, Japan')


if __name__ == '__main__':
    unittest.main()