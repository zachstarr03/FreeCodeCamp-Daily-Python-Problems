# 3/20:

""" Directions: Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.
"""

""" Time Complexity: O(n) -> all operations are of constant time. The input is always "HH:MM", a fixed length; there is no input scaling.
 Space Complexity: O(n) -> splitting the string creates a new list, but the list is of constant size everytime, where size = 2, since
 the input string is of a fixed-size. All other variables take up constant space in memory.
"""

def get_shadow(time):

    # initialize the time at noon
    noon_time = 12

    # split on the ':' to get the hours and minutes
    hours_split = int(time.split(":")[0])
    minutes_split = int(time.split(":")[1])

    # calculate the total minutes
    total_minutes = (hours_split * 60) + minutes_split

    # if minutes_split contains a value, convert total minutes back into hours (float)
    if minutes_split:
        hours = total_minutes / 60

    # if not, convert total minutes back into hours (int)
    else:
        hours = int(total_minutes / 60)

    # check if the time is before sunrise (6am), after sunset (6pm or later), or at noon, if so there is no shadow to caclulate
    if hours < 6 or hours >= 18 or hours == 12:
        return "No shadow"

    # if the time is before noon, the sun is in the East, so the direction of every shadow is West
    if hours < noon_time:
        direction = "west"

    # the sun is in the West, so the direction of every shadow is East
    else:
        direction = "east"

    # Calculate how many hours until noon, absolute value for if the time is after 12 (noon)
    # Calculate the total amount of feet the shadow is by cubing the value
    hours_until_noon = abs(noon_time - hours)
    total_feet = hours_until_noon**3

    # total feet and direction format
    return f"{total_feet}ft {direction}"

# main test cases
if __name__ == "__main__":
    print(get_shadow("10:00"))
    print(get_shadow("15:00"))
    print(get_shadow("12:00"))
    print(get_shadow("17:30"))
    print(get_shadow("05:00"))
    print(get_shadow("06:00"))
    print(get_shadow("18:00"))
    print(get_shadow("07:30"))
    print(get_shadow("00:00"))

""" I did not use any LLM for my solution. I worked through my reasoning and logic on my own accord.
"""