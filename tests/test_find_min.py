import unittest
import weather


class FindMinTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_find_min_positive(self):
        # these are integers but expecting a float to 1 decimal place & is the 0 position in the list i.e. its in 1st place
        temperatures = [49, 57, 56, 55, 53]
        expected_result = (49.0, 0)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_negative(self):
        # these are negative integers but expecting a negative float to 1 decimal place & is the 3 position in the list i.e. its in 4th place
        temperatures = [-10, -8, 2, -16, 4]
        expected_result = (-16.0, 3)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_floats(self):
        # these are floats returning a float with 1 decimal place & is the 3 position in the list i.e. its in 4th place
        temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
        expected_result = (8.9, 3)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_strings(self):
        # these are stings and returning a float with 1 decimal place & is the 5 position in the list i.e. its in 6th place
        temperatures = ["49", "57", "56", "55", "53", "49"]
        expected_result = (49.0, 5)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_empty_list(self):
        # this is an empty list returning a NONE or () and doesn't have a position
        # to handle empty lines or no expected results
        temperatures = []
        expected_result = ()
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_min_repeated_value(self):
        # these are integers returning a float to 1 decimal place & is the 5 position in the list i.e. its in 6th place
        temperatures = [49, 57, 56, 55, 53, 49]
        expected_result = (49.0, 5)
        result = weather.find_min(temperatures)
        self.assertEqual(result, expected_result)

