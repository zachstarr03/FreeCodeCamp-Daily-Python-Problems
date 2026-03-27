""" Directions: Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:

Letters	                   Width
"ilI"	                    1
"fjrt"	                    2
"abcdeghkmnopqsuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4
The table above includes all upper and lower case letters. Additionally:

Spaces (" ") have a width of 2

Periods (".") have a width of 1

If the given string is 50 units or less, return the string as-is, otherwise

Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over."""

""" Time Complexity: O(n) -> Must loop through the entire input string (n) to calculate the total width which is O(n) time.
As well as the second loop (which could potentially be needed) needs to be looped all the way through too to build the truncated string, 
which is also O(n). Since constants don't matter, time complexity is O(n).
Space Complexity: O(n) -> For the truncated result, a new string is being built (result). If the string is returned as-is, a copy is stored
on the entire input. The other variables and sets are constant space.
"""

# Different letter groups
group_1 = {'i', 'l', 'I', '.'}
group_2 = {'f', 'j', 'r', 't', " "}
group_3 = {'a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n', 'o',
           'p', 'q', 's', 'u', 'v', 'w', 'x', 'y', 'z', 'J', 'L'}
group_4 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

# help function to get the width of each letter in the string
def get_width(letter):
    if letter in group_1:
        return 1
    elif letter in group_2:
        return 2
    elif letter in group_3:
        return 3
    elif letter in group_4:
        return 4

def truncate_text(s):

    # variable to store the total width of the string
    total_units = 0

    # string of 3 periods to be added after truncating (fixed-length)
    period_string = "..."

    # increment through the input s and calculate its total width
    for letter in s:
        total_units += get_width(letter)

    # print(total_units)

    # if the total width is greater than or equal to 50, return the string as-is
    if total_units <= 50:
        return s

    # else, initialize a current width variable and result string. Then, increment through
    # the input string checking that the width + 3 (each period is 1 in width), is less than
    # or equal to 50. If so, concatenate each letter to the result string and total up the
    # current width until the else is hit and the loop breaks
    else:
        current_width = 0
        result = ""
        for letter in s:
            char_width = get_width(letter)
            if current_width + char_width + 3 <= 50:
                result += letter
                current_width += get_width(letter)
            else:
                break

    # concatenate the three periods to the end of the result string
    result += period_string

    return result

# main test cases
if __name__ == "__main__":
    print(truncate_text("The quick brown fox"))
    print(truncate_text("The silky smooth sloth"))
    print(truncate_text("THE LOUD BRIGHT BIRD"))
    print(truncate_text("The fast striped zebra"))
    print(truncate_text("The big black bear"))

""" I utilized an LLM to gather my logic and reasoning, but it did not derive a full solution for me.
My original approach was to made a giant dictionary of all the characters (keys) with their width values (values),
but I realized just using sets would be cleaner to read. 
"""

###################################################################################################################

"""
ChatGPT's optimal solution is below:

# Letter groups
group_1 = {'i', 'l', 'I', '.'}               # width 1
group_2 = {'f', 'j', 'r', 't', ' '}          # width 2
group_3 = {'a','b','c','d','e','g','h','k','m','n','o','p',
           'q','s','u','v','w','x','y','z','J','L'}  # width 3
group_4 = {'A','B','C','D','E','F','G','H','K','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z'}  # width 4

# Helper function
def get_width(letter):
    if letter in group_1:
        return 1
    elif letter in group_2:
        return 2
    elif letter in group_3:
        return 3
    elif letter in group_4:
        return 4

def truncate_text(s):
    limit = 50
    ellipsis_width = 3
    current_width = 0
    result = ""

    for letter in s:
        char_width = get_width(letter)
        # Check if adding this letter would exceed limit (reserve space for "..." if needed)
        if current_width + char_width > limit:
            break
        result += letter
        current_width += char_width

    # If total width exceeds limit, append "..."
    if current_width < sum(get_width(c) for c in s):  # string was truncated
        # make sure adding "..." does not exceed 50
        while current_width + ellipsis_width > limit:
            removed_char = result[-1]
            result = result[:-1]
            current_width -= get_width(removed_char)
        result += "..."
    
    return result
"""