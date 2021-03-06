import unittest
from leap_year import leap_year

test_cases = [
    ('Hello', "Hello is invalid year value."),
    (-1, "-1 is invalid year value."),
    (-0.01, "-0.01 is invalid year value."),
    (0, "0 is invalid year value."),
    (0.01, "0.01 is invalid year value."),
    (1, "1 is not leap year."),
    (2, "2 is not leap year."),
    (3, "3 is not leap year."),
    (4, "4 is leap year."),
    (5, "5 is not leap year."),
    (6, "6 is not leap year."),
    (7, "7 is not leap year."),
    (8, "8 is leap year."),
    (9, "9 is not leap year."),
    (10, "10 is not leap year."),
    (11, "11 is not leap year."),
    (12, "12 is leap year."),
    (100, "100 is century year."),
    (101, "101 is not leap year."),
    (102, "102 is not leap year."),
    (103, "103 is not leap year."),
    (104, "104 is leap year."),
    (105, "105 is not leap year."),
    (106, "106 is not leap year."),
    (107, "107 is not leap year."),
    (108, "108 is leap year."),
    (200, "200 is century year."),
    (300, "300 is century year."),
    (400, "400 is century leap year."),
    (1000, "1000 is century year."),
    (1001, "1001 is not leap year."),
    (1002, "1002 is not leap year."),
    (1003, "1003 is not leap year."),
    (1004, "1004 is leap year."),
    (2000, "2000 is century leap year."),
    (3000, "3000 is century year."),
    (4000, "4000 is century leap year."),
]


class LeapYearTestClass(unittest.TestCase):

    def test_year(self):
        for testcase in test_cases:
            (year, result) = testcase
            self.assertEqual(result, leap_year(year))


if __name__ == "__main__":
    unittest.main()
