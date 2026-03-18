# 3/18:

""" Directions: Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
"""

""" Time Complexity: O(n) -> splitting requires the entire string to be scanned, so as the input grows,
time complexity scales linearly with n. To create the new list each number must be processed, and the max()
also needs to scan the entire list to find the maximum value.
Space Complexity: O(n) -> to split the program needs to allocate new memory to store the resulting list, so O(n)
where n is the number of  characters being processed. Creating a new list in memory is O(n) as well since the
program must allocate new memory to store the new list.
"""

import re

def largest_number(s):

    # if a period ('.') exists in the original string, we are working with the
    # possibility of a float being the largest value
    period = "."

    # check if a period does NOT exist in the original string, if so split on the specified
    # separators and create a new list of integers
    if period not in s:
        s_split = re.split(r'[,!?:;]', s)
        # print(s_split)
        new_list = list(map(int, s_split))

    # check if a period DOES exist in the original string, if so split on the specified
    # separators and create a new list of floats
    else:
        s_split = re.split(r'[,!?:;]', s)
        # print(s_split)
        new_list = list(map(float, s_split))

    # use the max() to store the largest number in the list
    largest_num = max(new_list)

    return largest_num

# main test cases
if __name__ == "__main__":
    print(largest_number("1,2"))                                                            # 2
    print(largest_number("4;15:60,26?52!0"))                                                # 60
    print(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"))     # -402
    print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))                                   # 99.9

########################################################################################################
""" I did not use an LLM for help on this problem at all. Once I finished and got a solution, I checked
to see what the LLM's solution would look like to compare with mine.
"""

"""
ChatGPT's solution is below: time and space are both O(n) as well

import re

def largest_number(s):
    
    numbers = list(map(float, re.split(r'[,!?:;]', s)))
    result = max(numbers)
    return int(result) if result.is_integer() else result
"""

''' Once I saw this, I realized that Python can just handle everything as a float here safely, and there
isn't a need to check for the period; meaning I don't need the if/else logic block. This also helps avoid
calling "re.split" twice. Their version is more Pythonic, as it doesn't over-handle types. 

If you wanted to see the index of the largest value in the list, just use the .index() with largest_num
as the parameter
'''