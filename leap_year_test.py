import pytest
from leap_year import leap_year

from leap_year_unittest import test_cases


class TestLeapYear:

    @pytest.mark.parametrize('year result'.split(), test_cases)
    def test_year(self, year, result):
        assert result == leap_year(year)
