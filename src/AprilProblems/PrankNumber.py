# 4/01:


""" Directions: Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).

For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
"""

""" Time Complexity: O(n) -> as input n grows, time scales linearly. In the worst case, the wrong element could be at the end
of the array. The first loop computes the differences between values which is O(n), and the second loop finds and fixes the 
pattern which is also O(n). Both loops are sequential.
Space Complexity: O(n) -> a new array is created to store the differences which is of size n - 1. Due to this array,
space is O(n).
"""

import statistics

def fix_prank_number(arr):

    # array to store the differences between each value
    difference_arr = []

    # increment through the input arr, calculating the difference between each value
    # append each difference to the difference array for use later
    for index in range(len(arr) - 1):
        difference = arr[index + 1] - arr[index]
        difference_arr.append(difference)

        # print(difference)

    # print(difference_arr)

    # calculate what the correct difference is for the pattern
    most_frequent_difference = statistics.mode(difference_arr)
    # print(most_frequent_difference)

    # increment back through the array, checking if a difference between two values is not
    # equal to the most frequent one. If so, look ahead to decide which element is wrong,
    # if arr[index] is then do the next element - the difference, if arr[index + 1] is then
    # do the element before + the difference. Return the arr early once the number is fixed
    for index in range(len(arr) - 1):
        if arr[index + 1] - arr[index] != most_frequent_difference:
            if index + 2 < len(arr) and arr[index + 2] - arr[index + 1] == most_frequent_difference:
                arr[index] = arr[index + 1] - most_frequent_difference
            else:
                arr[index + 1] = arr[index] + most_frequent_difference

            return arr

    return arr

# main test cases
if __name__ == "__main__":
    print(fix_prank_number([2, 4, 7, 8, 10]))
    print(fix_prank_number([10, 10, 8, 7, 6]))
    print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
    print(fix_prank_number([4, 1, -2, -5, -8, -5]))
    print(fix_prank_number([0, 100, 200, 300, 150, 500]))
    print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
    print(fix_prank_number([-5, 5, 10, 15, 20]))

""" I utilized an LLM to help me work through my reasoning and logic. It did not write my solution for me. """

###############################################################################################################

"""
ChatGPT's optimal solution: time is O(n), space is now O(1)

def fix_prank_number(arr):
    # Step 1: determine correct difference using first 3 diffs
    d1 = arr[1] - arr[0]
    d2 = arr[2] - arr[1]
    d3 = arr[3] - arr[2]

    # majority vote for correct difference
    if d1 == d2 or d1 == d3:
        d = d1
    else:
        d = d2

    # Step 2: find and fix the incorrect element
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            # check next difference to decide which element is wrong
            if i + 2 < len(arr) and arr[i + 2] - arr[i + 1] == d:
                # arr[i] is wrong
                arr[i] = arr[i + 1] - d
            else:
                # arr[i+1] is wrong
                arr[i + 1] = arr[i] + d
            return arr  # stop immediately after fixing

    return arr
"""