# Calenders with python
import calendar
month = calendar.month(2026,4)
print(month)


year = calendar.calendar(2026)
print(year)

# Check if a year is a leap year
is_leap = calendar.isleap(2024)
print(is_leap)  # Output: True

# Get the weekday of a specific date
weekday = calendar.weekday(2024, 2, 29)
print(weekday)  # Output: 4 (Friday)


# Get the number of leap years in a range of years
leap_years = calendar.leapdays(2000, 2025)
print(leap_years)  # Output: 6 (2000, 2004, 2008, 2012, 2016, 2020)


# Get the first weekday of a month
first_weekday = calendar.monthrange(2024, 2)[0]
print(first_weekday)  # Output: 3 (Thursday)


# Get the number of days in a month
days_in_month = calendar.monthrange(2024, 2)[1]
print(days_in_month)  # Output: 29 (February in a leap year)


# Explain the calendar module
# The calendar module in Python provides functions to work with dates and calendars. It allows you to display calendars, check for leap years, and perform various date-related operations. You can use it to generate text calendars for specific months or years, determine the weekday of a given date, and calculate the number of leap years within a range of years. The module is useful for applications that require date manipulation and calendar-related functionality.
# For example, you can use the calendar module to create a calendar for a specific month, check if a year is a leap year, or find out how many days are in a particular month. It provides a convenient way to handle date-related tasks in Python.
# The calendar module also includes functions for working with different calendar systems, such as the Gregorian calendar and the Julian calendar. It can be used to perform date calculations, format dates, and generate calendars in various formats. Overall, the calendar module is a powerful tool for managing dates and calendars in Python programming.


# methods in calendar module
# 1. calendar.month(year, month): Returns a string representing the calendar for a specific month and year.
# 2. calendar.calendar(year): Returns a string representing the calendar for an entire year.
# 3. calendar.isleap(year): Returns True if the specified year is a leap year, otherwise returns False.
# 4. calendar.weekday(year, month, day): Returns the weekday of a specific date, where Monday is 0 and Sunday is 6.
# 5. calendar.leapdays(y1, y2): Returns the number of leap years in the range of years from y1 to y2 (exclusive).
# 6. calendar.monthrange(year, month): Returns a tuple containing the weekday of the first day of the month and the number of days in the month.
# These are some of the commonly used methods in the calendar module, which can help you work with dates and calendars effectively in Python.