
def is_leap_year(year):
    # div by 4 , not by 100, by 400
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
