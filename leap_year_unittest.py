import unittest
from leap_year import leap_year

test_cases = [
    (1, "1 is not leap year."),
    (2, "2 is not leap year."),
    (3, "3 is not leap year."),
    (4, "4 is leap year.")
]


class LeapYearTestClass(unittest.TestCase):

    def test_year(self):
        for testcase in test_cases:
            (year, result) = testcase
            self.assertEqual(result, leap_year(year))


if __name__ == "__main__":
    unittest.main()
