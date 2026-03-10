# 3/09:

""" Directions: Given an array of numbers, return the sum of all the numbers.
"""

""" Time Complexity: O(n) -> the length of the numbers list grows linearly (n), must increment through the entire list of n size. The loop will always run once for each element.
Space Complexity: O(1) -> Memory usage does not grow with n. Sum is one integer of constant space, i is the loop counter which is constant space. Regardless of how big the input list is, both are constant space.
"""

''' O(n) time complexity, O(1) space complexity '''
def sum_array(numbers):

    # initialize a variable to store the sum
    sum = 0

    # increment through the list of numbers, and sum each value at the ith index
    for i in range(len(numbers)):
        sum += numbers[i]

    return sum

# main: test cases
if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5]))                               # 15
    print(sum_array([42]))                                          # 42
    print(sum_array([5, -2, 7, -3]))                                # 7
    print(sum_array([203, 145, -129, 6293, 523, -919, 845, 2434]))  # 9395
    print(sum_array([0, 0]))                                        # 0

''' Incrementing through a list of size n, will always yield a time complexity of O(n). If the input size is n, the loop runs n times. 
Because Big O describes the general growth pattern and not just one input size, even if there is only one element (n = 1), the algorithm will still be O(n),
since it must check every element and always scale with n '''

##############################################################################################

"""
''' I didn't use an LLM for this problem for any guidance or help to develop my solution '''

''' Optimal Solution from ChatGPT: '''
def sum_array(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
"""