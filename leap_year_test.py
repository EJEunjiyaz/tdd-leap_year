import unittest
from leap_year import leap_year

test_cases = [('1',False)]

class LeapYearTestClass(unittest.TestCase):
     
    def test_Leap_Year(self):
        for testcase in test_cases:
            (year, result) = testcase
            self.assertEqual(result, leap_year(year))
 
if __name__ == "__main__":
    unittest.main() 