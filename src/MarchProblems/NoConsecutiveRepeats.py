# 3/23:

""" Directions: Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.
"""

""" Time Complexity: O(n) -> at the worst case, repeats might be at the very end of the string, so all n - 1 pairs need to be checked.
Each character needs to be checked to know if it repeats, therefore time can never be constant.
Space Complexity: O(1) -> No memory is growing with the input size, as no extra data structures are initialized, therefore we have
constant space.
"""

def has_no_repeats(s):

    # increment through the input string, using len(s) - 1 for the last iteration
    # if the current char is equal to the next char in the string, return False
    for char in range(len(s) - 1):
        if s[char] == s[char + 1]:
            return False

    return True

# main test cases
if __name__ == "__main__":
    print(has_no_repeats("hi world"))
    print(has_no_repeats("hello world"))
    print(has_no_repeats("abcdefghijklmnopqrstuvwxyz"))
    print(has_no_repeats("freeCodeCamp"))
    print(has_no_repeats("The quick brown fox jumped over the lazy dog."))
    print(has_no_repeats("Mississippi"))

""" No LLM was utilized to help me throughout this problem, I thought of my solution and iterated through my
logic and reasoning by myself. 
"""