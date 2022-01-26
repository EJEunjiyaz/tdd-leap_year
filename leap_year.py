def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return f'{year} is century year.' 
        return f'{year} is leap year.'
    return f'{year} is not leap year.'
