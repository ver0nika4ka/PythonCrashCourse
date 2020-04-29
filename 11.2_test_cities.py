import unittest
from city_functions_11_2 import get_city_country

class NamesTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country_name(self):
        """Do Tokyo, Japan works?"""
        full_name = get_city_country('tokyo', 'japan')
        self.assertEqual(full_name, 'Tokyo, Japan')

    def test_city_country_population(self):
        """Do Tokyo, Japan population: 126 million. works?"""
        result = get_city_country('tokyo', 'japan', '126 million')
        self.assertEqual(result, 'Tokyo, Japan – population: 126 million.')


if __name__ == '__main__':
    unittest.main()