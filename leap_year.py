def leap_year(year):
    if type(year) is not int or year <= 0:
        return f'{year} is invalid year value.'
    elif year % 400 == 0:
        return f'{year} is century leap year.'
    elif year % 100 == 0:
        return f'{year} is century year.'
    elif year % 4 == 0:
        return f'{year} is leap year.'
    return f'{year} is not leap year.'
