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


def firstyear(day, month, year):
    i = 12
    days = 0
    while (i - month > 0):
        days = days + monthArray[i - 1]
        i = i - 1
    days = days + monthArray[month - 1] - day
    return days


def lastyear(day, month, year):
    i = 1
    days = 0
    while (month - i > 0):
        days = days + monthArray[i - 1]
        i = i + 1
    days = days + day
    return days


def firstyear_leap(day, month, year):
    i = 12
    days = 0
    while (i - month > 0):
        days = days + monthArrayLeap[i - 1]
        i = i - 1
    days = days + monthArrayLeap[month - 1] - day
    return days


def lastyear_leap(day, month, year):
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


def same_year_days(birth_day, birth_month,
                   birth_year, today_day,
                   today_month, today_year):
    if birth_month == today_month:
        days = today_day - birth_day
        return days
    else:
        if leapyear(birth_year):
            days = days + \
                firstyear_leap(birth_day, birth_month, birth_year) \
                - firstyear_leap(today_day, today_month, today_year)
        else:
            days = days + \
                firstyear(birth_day, birth_month, birth_year) \
                - firstyear(today_day, today_month, today_year)


def age_in_days(birth_day, birth_month, birth_year,
                today_day, today_month, today_year):
    days = 0
    if birth_year == today_year:
        days = days + \
            same_year_days(birth_day, birth_month,
                           birth_year, today_day,
                           today_month, today_year)
        return days

    if leapyear(birth_year):
        days = days + firstyear_leap(birth_day, birth_month, birth_year)
    else:
        days = days + firstyear(birth_day, birth_month, birth_year)

    days = days + middle_year_days(birth_year, today_year)

    if leapyear(today_year):
        days = days + lastyear_leap(today_day, today_month, today_year)
    else:
        days = days + lastyear(today_day, today_month, today_year)

    return days

#show result
print age_in_days(14, 8, 1972, 13, 1, 2014)

print age_in_days(14, 8, 1972, 31, 8, 1972)
