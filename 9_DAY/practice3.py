# Getting currunt date and time
import datetime
current_date_time = datetime.datetime.now()
print(current_date_time)



# Getting current date
current_date = datetime.date.today()
print(current_date) 



# Getting current time  
current_time = datetime.datetime.now().time()
print(current_time)



# Getting current year, month, day, hour, minute, second
current_year = current_date_time.year
current_month = current_date_time.month
current_day = current_date_time.day
current_hour = current_date_time.hour
current_minute = current_date_time.minute
current_second = current_date_time.second
print(f"Current Year: {current_year}")
print(f"Current Month: {current_month}")
print(f"Current Day: {current_day}")
print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Current Second: {current_second}")




# Formatting date and time
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date_time)  # Output: 2024-06-01 12:30:45 (example output)




# Parsing date and time from a string
date_time_string = "2024-06-01 12:30:45"
parsed_date_time = datetime.datetime.strptime(date_time_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date_time)  # Output: 2024-06-01 12:30:45




# Date arithmetic
from datetime import timedelta
# Adding 7 days to the current date
future_date = current_date + timedelta(days=7)
print(future_date)  # Output: 2024-06-08 (example output)
# Subtracting 7 days from the current date
past_date = current_date - timedelta(days=7)
print(past_date)  # Output: 2024-05-25 (example output)


# Getting the difference between two dates
date1 = datetime.date(2024, 6, 1)
date2 = datetime.date(2024, 6, 15)
date_difference = date2 - date1
print(date_difference)  # Output: 14 days, 0:00:00 (example output)



# Explain the datetime module
# The datetime module in Python provides classes for manipulating dates and times. It allows you to work with date and time objects, perform arithmetic operations on them, and format them in various ways. The module includes classes such as datetime, date, time, and timedelta, which provide methods for creating, manipulating, and formatting date and time values. You can use the datetime module to get the current date and time, perform calculations with dates and times, and format them for display. It is a powerful tool for handling date and time-related tasks in Python programming.
# The datetime module also provides functions for parsing date and time strings, converting between different date and time formats, and handling time zones. It is widely used in applications that require date and time manipulation, such as scheduling, logging, and data analysis. Overall, the datetime module is an essential part of Python's standard library for working with dates and times effectively.
# Methods in datetime module
# 1. datetime.now(): Returns the current local date and time as a datetime object.
# 2. date.today(): Returns the current local date as a date object.
# 3. datetime.strptime(date_string, format): Parses a date string into a datetime object based on the specified format.
# 4. datetime.strftime(format): Returns a string representation of the datetime object based on the specified format.
# 5. timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Represents a duration, the difference between two dates or times.
# 6. datetime.date(year, month, day): Creates a date object with the specified  year, month, and day.
# 7. datetime.time(hour=0, minute=0, second=0, microsecond=0): Creates a time object with the specified hour, minute, second, and microsecond.
# These are some of the commonly used methods in the datetime module, which can help you work with dates and times effectively in Python programming.