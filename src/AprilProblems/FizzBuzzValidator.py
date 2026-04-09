# 4/08:

""" Directions: Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.
"""

""" Time Complexity: O(n) -> For the first loop, the worst case would have the first integer in the sequence as the last element,
meaning the loop must iterate through all elements of n. For the second loop, the worst case is when the array is valid, meaning
the loop must iterate through all n elements to check the sequence. Both loops are O(n), because as the input grows, time complexity
grows linearly.
Space Complexity: O(1) -> Only a couple variables are being stored in memory and they're all of constant space. There are no extra data
structures being created proportional to the input.
"""

def is_fizz_buzz(arr):

    # set the starting value to None
    starting_value = None

    # increment through arr on index and value, find the first integer present in the
    # list and by using its value and index, determine the starting value of the list
    for index, value in enumerate(arr):
        # print(value, index)
        if isinstance(value, int) and starting_value is None:
            starting_value = value - index
            break

    # if no integer is found within the arr, the list cannot be validated
    if starting_value is None:
        return False

    # increment back through the arr and calculate the next value in the arr. Then check
    # if the next value is a multiple of both 3 and 5, just 3, or just 5 and if so set the
    # expected_value string to the correct replacement for validating. If none of those, the
    # expected_value is just set to the next value
    for index, value in enumerate(arr):
        next_value = starting_value + index

        if next_value % 3 == 0 and next_value % 5 == 0:
            expected_value = "FizzBuzz"
        elif next_value % 3 == 0:
            expected_value = "Fizz"
        elif next_value % 5 == 0:
            expected_value = "Buzz"
        else:
            expected_value = next_value

        # if an index in the arr is not what is expected, the sequence is false, otherwise true
        if arr[index] != expected_value:
            return False

    return True

# main test cases
if __name__ == "__main__":
    print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))
    print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
    print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))
    print(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]))
    print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]))
    print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]))
    print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]))

""" I utilized an LLM for some help with grasping my idea at first and logic. From there, I constructed my solution.
It did not hand me the solution
"""

#####################################################################################################################

"""
ChatGPT's optimal solution (performance): time and space are the same still

def is_fizz_buzz(arr):
    # find the first integer to determine the start
    for index, value in enumerate(arr):
        if isinstance(value, int):
            starting_value = value - index
            break
    else:
        # no integer found
        return False

    # validate the sequence
    for i, value in enumerate(arr):
        num = starting_value + i
        if num % 15 == 0:
            expected = "FizzBuzz"
        elif num % 3 == 0:
            expected = "Fizz"
        elif num % 5 == 0:
            expected = "Buzz"
        else:
            expected = num

        if value != expected:
            return False

    return True
"""