import unittest
import weather


class FindMaxTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_find_max_positive(self):
        # these are integers returning a float to 1 decimal place and its in position 1 which is 2nd place
        temperatures = [49, 57, 56, 55, 53]
        expected_result = (57.0, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_negative(self):
        # these are negative integers returning a float to 1 decimal place and its in position 4 which is 5th place
        temperatures = [-10, -8, 2, -16, 4]
        expected_result = (4.0, 4)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_floats(self):
        # these are floats returning a float to 1 decimal place and its in position 1 which is 2nd place
        temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
        expected_result = (14.5, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_strings(self):
        # these are strings returning a float to 1 decimal place and its in position 1 which is 2nd place
        # must convert str into int
        temperatures = ["49", "57", "56", "55", "53", "49"]
        expected_result = (57.0, 1)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_empty_list(self):
        # this is an empty list returning a NONE or () and doesn't have a position
        # to handle empty lines or no expected results
        temperatures = []
        expected_result = ()
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)

    def test_find_max_repeated_value(self):
        # these are integers returning a float to 1 decimal place and its in position 4 which is 5th place
        temperatures = [49, 57, 56, 55, 57, 53, 49]
        expected_result = (57.0, 4)
        result = weather.find_max(temperatures)
        self.assertEqual(result, expected_result)
