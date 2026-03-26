# 3/26:

""" Directions: Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.
"""

""" Time Complexity: O(1) -> Dictionary lookup and string slicing are both constant time operations, and there
are a fixed number of operations in the program.
Space Complexity: O(1) -> The dictionary has a fixed number of entries (each day = 7 days), therefore it does not
grow with the input size, and is constant space.
"""

def get_movie_night_cost(day, showtime, number_of_tickets):

    # variable to store the total cost
    total_ticket_price = 0

    # dictionary to map each day of the week with its ticket price
    cost_by_day = {
                   "Monday": 10, "Tuesday": 5, "Wednesday": 10, "Thursday": 10,
                   "Friday": 12, "Saturday": 12, "Sunday": 12
                  }

    # check if the length of the showtime string is 7, if so then index 0 to 2
    # will give the hour, else index 0 to 1 will give the hour
    if len(showtime) == 7:
        showtime_hour = int(showtime[0:2])
    else:
        showtime_hour = int(showtime[0:1])

    # check if the day is in the dictionary
    # Case 1: If the showtime is after 5:00pm, ticket prices stay unchanged
    # Case 2: If the showtime is before 5:00pm and the day isn't Tuesday, subtract $2 per ticket
    # Case 3: Else the day is Tuesday, just calculate its normal ticket price
    if day in cost_by_day:
        if "pm" in showtime and showtime_hour >= 5:
            total_ticket_price = cost_by_day[day] * number_of_tickets
        elif ("am" in showtime or ("pm" in showtime and showtime_hour < 5)) and day != "Tuesday":
            total_ticket_price = (cost_by_day[day] - 2) * number_of_tickets
        else:
            total_ticket_price = cost_by_day[day] * number_of_tickets

    # return the total ticket price rounded to 2 decimal points and in the correct format
    return f"${total_ticket_price:.2f}"

# main test cases
if __name__ == "__main__":
    print(get_movie_night_cost("Saturday", "10:00pm", 1))
    print(get_movie_night_cost("Sunday", "10:00am", 1))
    print(get_movie_night_cost("Tuesday", "7:20pm", 2))
    print(get_movie_night_cost("Wednesday", "5:40pm", 3))
    print(get_movie_night_cost("Monday", "11:50am", 4))
    print(get_movie_night_cost("Friday", "4:30pm", 5))
    print(get_movie_night_cost("Tuesday", "11:30am", 1))

""" I didn't utilize an LLM at all when crafting my solution, all the logic and reasoning is my own. After I finished,
I compared my solution with ChatGPT's to see how optimal it was versus theirs.
"""

######################################################################################################################

"""
ChatGPT's solution: time and space are the same
    
def get_movie_night_cost(day, showtime, number_of_tickets):
    cost_by_day = {
        "Monday": 10, "Tuesday": 5, "Wednesday": 10, "Thursday": 10,
        "Friday": 12, "Saturday": 12, "Sunday": 12
    }

    # Extract hour and period
    showtime_hour = int(showtime.split(":")[0])
    period = showtime[-2:]  # "am" or "pm"

    # Tuesday flat pricing
    if day == "Tuesday":
        total = 5 * number_of_tickets
    else:
        base_price = cost_by_day[day]

        # Check if matinee (before 5pm)
        is_matinee = (period == "am") or (period == "pm" and showtime_hour < 5)

        if is_matinee:
            base_price -= 2

        total = base_price * number_of_tickets

    return f"${total:.2f}"
"""

""" I understood all the improvements it made and the optimization, which makes it easier to read. """