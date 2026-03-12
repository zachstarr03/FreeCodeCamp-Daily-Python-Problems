""" Directions: Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
For the chain to be valid, the second number of each domino must match the first number of the next domino.
The first number of the first domino and the last number of the last domino don't need to match anything.
"""

""" Time Complexity: O(n) -> if there are n dominoes, the loop will run n - 1 times. The loop iterates through
 the dominoes once, comparing each domino with the next domino.
 Space Complexity: O(1) -> a couple variables are used and stored in memory, there is no new array being created
 or data from the array being copied. 
 """

''' At first glance, I thought about flattening the array, but I realized working with the 2D array was much easier, as
each pair represents a single domino. Flattening the array would have made things more confusing because I would have lost 
the pair structure. If I flattened the array, the space complexity would have been O(n) instead, since flattening an array
creates a copy of the original array in memory. 
'''

def is_valid_domino_chain(dominoes):

    # a single pair represents one domino, need to compare a domino's second element,
    # with the first element of the next domino

    # iterate through the 2D array, comparing the second number of the current domino, with
    # the first number of the next domino
    for i in range(len(dominoes) - 1):
        current_domino = dominoes[i]
        next_domino = dominoes[i + 1]
        # print(current_domino[1])
        if current_domino[1] != next_domino[0]:             # compare the two consecutive elements
            # print(current_domino[1], next_domino[0])
            return False

    return True

''' Conceptually, the inside of the loop looks like this:  if dominoes[i][1] != dominoes[i + 1][0] '''

# main test cases
if __name__ == "__main__":
    print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]))  # True
    print(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]))  # False
    print(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]))  # False
    print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]))  # True
    print(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]))  # False

''' An LLM helped understand an approach to this problem, and helped me work through my reasoning and logic. It
did not give me the solution, I interfere and developed a solution on my own.
'''