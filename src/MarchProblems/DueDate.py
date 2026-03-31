# 3/30:

""" Directions: Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month.
"""

""" Time Complexity: O(1) -> the date string is always of a fixed length, therefore the .split() is constant time.
All the other operations are also constant time, therefore overall the time complexity is O(1).
Space Complexity: O(1) -> the .split() creates a list of 3 strings, this is always the same since the input is a fixed
length. All the other operations are also constant time, therefore the overall space complexity is O(1).
"""

import calendar

def get_due_date(date_str):

    date = date_str.split("-")
    # print(date)

    # store the year, month and day as a integer
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    # store the additional 9 months, calculate the new month, and initialize the years to add
    future_months = 9
    new_month = month + future_months
    years_to_add = 0

    # if the new month is greater than 12, calculate the necessary amount of years to add,
    # with integer division and wrap the months with modulo (%) 12
    if new_month > 12:
        years_to_add = new_month // 12
        new_month = new_month % 12

    # print(years_to_add)
    # print(new_month)

    # calculate the new year
    new_year = year + years_to_add
    # print(new_year)

    # weekday is ignored ('_'), I only care about the number of days (last_day) in each month
    _, last_day = calendar.monthrange(new_year, new_month)

    # the new day takes the minimum value of either the original day or the last day of the month
    new_day = min(day, last_day)

    # store the newly formatted date
    new_date = f"{new_year:04d}-{new_month:02d}-{new_day:02d}"

    return new_date

# main test cases
if __name__ == "__main__":
    print(get_due_date("2025-03-30"))
    print(get_due_date("2025-04-27"))
    print(get_due_date("2025-05-29"))
    print(get_due_date("2026-06-30"))
    print(get_due_date("2026-10-11"))

""" I utilized an LLM to help me get going and understand my own reasoning and logic. It did not help generate
a solution for me.
"""

###################################################################################################################

"""
ChatGPT's optimal solution: time complexity and space are the same
import calendar

def get_due_date(date_str, months_to_add=9):
    # Parse the date
    year, month, day = map(int, date_str.split("-"))
    
    # Compute total months
    total_months = month + months_to_add
    
    # Compute new year and month in one step
    new_year = year + (total_months - 1) // 12
    new_month = (total_months - 1) % 12 + 1
    
    # Get last valid day of the new month
    _, last_day = calendar.monthrange(new_year, new_month)
    
    # Clamp day to the last day of the month
    new_day = min(day, last_day)
    
    # Format result as YYYY-MM-DD
    return f"{new_year:04d}-{new_month:02d}-{new_day:02d}"
"""