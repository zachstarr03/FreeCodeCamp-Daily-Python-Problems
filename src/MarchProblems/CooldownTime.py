# 3/25:

""" Directions:Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
"""

""" Time Complexity: O(1) -> The two input strings are always a fixed length, therefore the amount of work
never grows, and we have constant time.
Space Complexity: O(1) -> .strptime() creates a fixed number of objects and none of them depend on the input size,
therefore memory is not growing with input, and we have constant space.
"""

from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    parse_on = "%Y-%m-%dT%H:%M:%S"

    # Parses the two strings into a structured object -> "2026-03-31T08:00:00" becomes
    # datetime(2026, 3, 23, 8, 0, 0)
    finish = datetime.strptime(finish_time, parse_on)
    current = datetime.strptime(current_time, parse_on)

    # check if the current time minus the finish time is greater than or equal to 48 hours
    if current - finish >= timedelta(hours=48):
        return True
    else:
        return False

# main test cases
if __name__ == "__main__":
    print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
    print(can_retake("2026-04-24T14:00:00", "2026-03-25T10:00:00"))
    print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
    print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))

""" At first, my approach was to slice the timestamps into pieces and compare components. I recognized a fundamental
 flaw in my approach, which was that time doesn't allow you to compare individual components individually; it doesn't work
 like that. With slicing, my conditional logic was flawed if the timestampes came down to only being a second short of 48
 hours. My reasoning path was fragile, and there were edge cases, such as if the current timestamp went into a new month,
 but only by a day; my logic would still believe 48 hours have passed. 
 
 I utilized an LLM to reason through my logic and understand were my code would break on edge cases, that is when I realized
 I could use the datetime library Python has to allow Python to do all of the time lapse checks. Using datetime allows Python
 to convert the timestamps into points on a timeline and compared the elapsed time. This isn't pieces of the time like I was
 dealing with by slicing, it is a single point in time now which is easily comparable with timedelta. There is no need to worry
 about if the hour is greater than or equal to the other hour, or seconds, or if the month changes. Python handles all this
 internally with datetime. All edge cases are handled automatically this way. Once I understood how datetime operates and its
 capabilities, I wrote my program and got my solution. I could have sticked with slicing and converted each timestamp into a single
 unit like seconds, but at that point its basically the same as using datetime.
 """