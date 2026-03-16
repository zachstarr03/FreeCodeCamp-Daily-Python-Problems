# 3/16:

""" Directions: Given two integers, determine if you can evenly divide the first one
by the second one.
"""

""" Time Complexity: O(1) -> None of the operations performed depend on input size or loops, the input size does not grow.
Space Complexity: O(1) -> Memory usage does not scale with the input size either. 
"""

def is_evenly_divisible(a, b):

    # division by 0 check
    if b == 0:
        raise ValueError("Cannot divide by zero")

    # if the remainder is 0, the first integer can evenly be divided by the second integer
    return a % b == 0

# main test cases
if __name__ == "__main__":
    print(is_evenly_divisible(4, 2))        # True
    print(is_evenly_divisible(7, 3))        # False
    print(is_evenly_divisible(5, 10))       # False
    print(is_evenly_divisible(48, 6))       # True
    print(is_evenly_divisible(3186, 9))     # True
    print(is_evenly_divisible(4192, 11))    # False