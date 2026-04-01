# 3/31:

""" Directions: Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.
"""

""" Time Complexity: O(1) -> The input size is always a fixed size and the program always does a fixed number of
operations. Regardless of the input, the runtime is never growing.
Space Complexity: O(1) -> All variables being stored in memory are constant space and there are no additional data
structures that scale with the input.
"""

def alarm_check(alarm_time, wake_time):

    # split the alarm time and wake time on the colon (':') to retrieve the hour and minute
    alarm_time_hour, alarm_time_minute = alarm_time.split(":")
    wake_time_hour, wake_time_minute = wake_time.split(":")

    # turn the alarm time and wake time into total minutes for easier use later
    alarm_time_total = int(alarm_time_hour) * 60 + int(alarm_time_minute)
    wake_time_total = int(wake_time_hour) * 60 + int(wake_time_minute)

    # calculate the total minutes difference
    total_time_difference = wake_time_total - alarm_time_total

    # variable to store the snooze time
    snooze_window = 10

    # check if you woke up before, on time or late
    if total_time_difference < 0:
        return "early"
    elif total_time_difference <= snooze_window:
        return "on time"
    else:
        return "late"

# main test cases
if __name__ == "__main__":
    print(alarm_check("07:00", "06:45"))
    print(alarm_check("06:30", "06:30"))
    print(alarm_check("08:10", "08:15"))
    print(alarm_check("09:30", "09:45"))
    print(alarm_check("08:15", "08:25"))
    print(alarm_check("05:45", "05:56"))
    print(alarm_check("04:30", "04:00"))

""" I did not utilize an LLM for help with my reasoning or logic at all. """

#############################################################################

"""
ChatGPT's optimal solution (readability): time and space are the same

def alarm_check(a, w):
    to_min = lambda t: int(t[:2]) * 60 + int(t[3:])
    diff = to_min(w) - to_min(a)
    return "early" if diff < 0 else "on time" if diff <= 10 else "late"
"""