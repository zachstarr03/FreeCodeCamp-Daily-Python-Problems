# 3/29:

""" Directions: Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

The first 9 characters must be digits, and
The final character may be a digit or the letter "X", which represents the number 10.
To validate it:

Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
Add all the results together.
If the total is divisible by 11, it's valid.
"""

""" Time Complexity: O(n) -> You must scan the entire string, and all the operations inside the loop are O(1)
(if checks, and arithmetic).
Space Complexity: O(n) -> .replace() creates a new string in memory, therefore space is O(n).
"""

def is_valid_isbn10(s):

    # char to remove in the original string
    remove_hyphen = '-'

    # new string with the hyphens removed
    new_s = s.replace(remove_hyphen, "")
    # print(new_s)

    # if the string isn't 10 digits, then return False
    if len(new_s) != 10:
        return False

    # variable to store the total for validation
    total = 0

    # increment through the string, keep tracking of its index and char. If a char is equal
    # to 'X' and it isn't positioned at index 9, return False ('X' is not in a valid spot).
    # Otherwise, set the 'X' to '10', else if every char is a digit (0-9) then store its value as an int
    for index, char in enumerate(new_s):
        if char == "X":
            if index != 9:
                return False
            new_value = 10
        elif char.isdigit():
            new_value = int(char)
        else:
            return False

        # multiply each digit by its position + 1
        total += new_value * (index + 1)

    # print(total)

    # check if the total is divisible by 11, if so return True (valid ISBN-10)
    if total % 11 == 0:
        return True
    else:
        return False

# main test cases
if __name__ == "__main__":
    print(is_valid_isbn10("0-306-40615-2"))
    print(is_valid_isbn10("0-306-40615-1"))
    print(is_valid_isbn10("0-8044-2957-X"))
    print(is_valid_isbn10("X-306-40615-2"))
    print(is_valid_isbn10("0-6822-2589-4"))

""" I utilized an LLM to help me check if I was on the right track with my own reasoning and logic, at first. 
My solution is fully my own.
"""

##############################################################################################################

"""
ChatGPT's optimal solution: time complexity is the same, but space is O(1) (no .replace()).

    def is_valid_isbn10(s):
    total = 0
    position = 0  # tracks valid ISBN position (1–10)

    for char in s:
        if char == "-":
            continue

        if position >= 10:
            return False  # too many characters

        if char == "X":
            if position != 9:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total += value * (position + 1)
        position += 1

    return position == 10 and total % 11 == 0
"""