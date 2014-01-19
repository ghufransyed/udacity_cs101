# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

monthArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthArrayLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# identifying leap years
# every 4 year
# EXCEPT if divisible by 100 UNLESS also divisible by 400


def leapyear(year):
    if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
        return True
    False


def firstyear(year, month, day):
    i = 12
    days = 0
    while (i - month > 0):
        days = days + monthArray[i - 1]
        i = i - 1
    days = days + monthArray[month - 1] - day
    return days


def lastyear(year, month, day):
    i = 1
    days = 0
    while (month - i > 0):
        days = days + monthArray[i - 1]
        i = i + 1
    days = days + day
    return days


def firstyear_leap(year, month, day):
    i = 12
    days = 0
    while (i - month > 0):
        days = days + monthArrayLeap[i - 1]
        i = i - 1
    days = days + monthArrayLeap[month - 1] - day
    return days


def lastyear_leap(year, month, day):
    i = 1
    days = 0
    while (month - i > 0):
        days = days + monthArrayLeap[i - 1]
        i = i + 1
    days = days + day
    return days


def middle_year_days(start_year, finish_year):
    year = start_year + 1
    days = 0
    while year < finish_year:
        if (leapyear(year)):
            days = days + 366
        else:
            days = days + 365
        year = year + 1
    return days


def same_year_days(year1, month1, day1, year2, month2, day2):
    if month1 == month2:
        days = day2 - day1
        return days
    else:
        if leapyear(year1):
            days = firstyear_leap(year1, month1, day1) \
                - firstyear_leap(year2, month2, day2)
            return days
        else:
            days = firstyear(year1, month1, day1) \
                - firstyear(year2, month2, day2)
            return days


def daysBetweenDates(year1, month1, day1,
                     year2, month2, day2):
    days = 0
    if year1 == year2:
        days = same_year_days(year1, month1, day1, year2, month2, day2)
        return days

    if leapyear(year1):
        days = days + firstyear_leap(year1, month1, day1)
    else:
        days = days + firstyear(year1, month1, day1)

    days = days + middle_year_days(year1, year2)

    if leapyear(year2):
        days = days + lastyear_leap(year2, month2, day2)
    else:
        days = days + lastyear(year2, month2, day2)

    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28),  58),
                  ((2012, 1, 1, 2012, 3, 1),  60),
                  ((2011, 6, 30, 2012, 6, 30),  366),
                  ((2011, 1, 1, 2012, 8, 8),  585),
                  ((1900, 1, 1, 1999, 12, 31),  36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
