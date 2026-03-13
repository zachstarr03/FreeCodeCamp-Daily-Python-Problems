# 3/13:

""" Directions: Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.
"""

""" Time Complexity: O(1) -> The input is always of "HH:MM" format, therefore the same number of steps are always taken.
There are no data structures growing with the input, loops or recursion, so the runtime never is scaling.
Space Complexity: O(1) -> A constant number of variables are stored in memory, and memory is never growing with input size.
"""

import math

def calculate_parking_fee(park_time, pickup_time):

    # total cost
    total_cost = 0

    # Rules:

    # $3 per hour, $10 overnight, $5 minimum
    price_per_hour = 3
    overnight_fee = 10
    minimum_fee = 5

    # split park_time and pickup_time to derive HH and MM
    park_time = park_time.split(":")
    # print(park_time)

    pickup_time = pickup_time.split(":")
    # print(pickup_time)

    # HH and MM format for each time
    park_time_hours = int(park_time[0])
    park_time_minutes = int(park_time[1])
    pickup_time_hours = int(pickup_time[0])
    pickup_time_minutes = int(pickup_time[1])

    # Calculate total minutes for both times
    park_time_total_minutes = (park_time_hours * 60) + park_time_minutes
    # print(park_time_total_minutes)

    pickup_time_total_minutes = (pickup_time_hours * 60) + pickup_time_minutes
    # print(pickup_time_total_minutes)

    ''' check for overnight parking, if so add the overnight fee, and calculate total minutes,
    else calculate total minutes normally '''
    if pickup_time_total_minutes < park_time_total_minutes:
        # print("midnight has passed")
        total_cost += overnight_fee
        total_minutes = (24 * 60 - park_time_total_minutes) + pickup_time_total_minutes
    else:
        total_minutes = pickup_time_total_minutes - park_time_total_minutes

    # convert total minutes to total hours, and round
    total_hours = total_minutes / 60
    total_hours_rounded = math.ceil(total_hours)
    # print(total_hours_rounded)

    # Calculate the total cost with the rounded hours and price per hour
    total_cost += total_hours_rounded * price_per_hour

    # check if the total cost is less than the minimum fee, if so total cost is now the minimum parking fee
    if total_cost < minimum_fee:
        total_cost = minimum_fee

    # return a string of total_cost with the '$' sign
    return "$" + str(total_cost)

# main test cases
if __name__ == "__main__":
    print(calculate_parking_fee("09:00", "11:00"))  # $6
    print(calculate_parking_fee("10:00", "10:30"))  # $5
    print(calculate_parking_fee("08:10", "10:45"))  # $9
    print(calculate_parking_fee("14:40", "23:10"))  # $27
    print(calculate_parking_fee("18:15", "01:30"))  # $34
    print(calculate_parking_fee("11:11", "11:10"))  # $82

''' An LLM helped me grasp my reasoning and logic, and explain if I was on the correct path towards a solution. 
It did not write or give me the solution, I wrote everything on my own with my own reasoning and logic.
'''

###############################################################################################################

''' ChatGPT's solution: O(1) for both time and space as well '''

"""
import math

def calculate_parking_fee(park_time, pickup_time):
    
    park_hour, park_min = map(int, park_time.split(":"))
    pickup_hour, pickup_min = map(int, pickup_time.split(":"))
    
    p = park_hour*60 + park_min
    r = pickup_hour*60 + pickup_min

    overnight = r < p
    if overnight:
        r += 1440       # 24 * 60

    hours = math.ceil((r - p)/60)

    cost = hours*3 + (10 if overnight else 0)
    cost = max(cost, 5)

    return "$" + str(cost)

if __name__ == "__main__":
    print(calculate_parking_fee("09:00", "11:00"))  # $6
    print(calculate_parking_fee("10:00", "10:30"))  # $5
    print(calculate_parking_fee("08:10", "10:45"))  # $9
    print(calculate_parking_fee("14:40", "23:10"))  # $27
    print(calculate_parking_fee("18:15", "01:30"))  # $34
    print(calculate_parking_fee("11:11", "11:10"))  # $82

"""