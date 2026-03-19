# 3/19:

""" Directions: Given a matrix (an array of arrays) filled with two distinct values,
return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]
Return:

[
  ["b", "a"],
  ["b", "b"]
]
"""

""" Time Complexity: O(m * n) -> O(N): The matrix contains m rows and n columns so at worst, scanning the entire matrix would
take O(m * n) time. Building the new matrix also increments over all the elements in the worst case, so O(m * n).
The time complexity simplifies to O(N), as it grows linearly as the total amount of elements inside the matrix grow (O(N) = O(m * n))
Space Complexity: O(m * n) -> O(N): A new matrix was created of the same size as the original matrix (m * n), so the amount of
space needed for all the elements is m * n. Since an entire new matrix is being stored, it's proportional to the total
number of elements.
"""

def invert_matrix(matrix):

    # if no elements exist in the matrix, return None (edge case when there are no elements)
    if len(matrix) == 0:
        print('No elements in the matrix')
        return None

    # store the two distinct values, val1 will always be the first value in the matrix
    val1 = matrix[0][0]
    val2 = None

    # increment through the rows in the matrix and the elements in each row, if the value
    # in a row is NOT equal to the first distinct value, then set val2 to this new value
    for row in matrix:
        for value in row:
            if value != val1:
                val2 = value
                break

    # print(val1, val2)

    # empty list for the new matrix
    new_matrix = []

    # increment through the rows again, create an empty list for the rows, increment through
    # each element in the row, and if the value at that element is equal to val1, append val2
    # to the new rows list, else append val1, and append this new rows list to the new matrix
    # to create the new matrix with val1 and val2 swapped
    for row in matrix:
        new_row = []
        for value in row:
            if value == val1:
                new_row.append(val2)
            else:
                new_row.append(val1)

        new_matrix.append(new_row)

    return new_matrix

# main test cases
if __name__ == "__main__":
    print(invert_matrix([["a", "b"], ["b", "b"]]))
    print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))
    print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]))
    print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]))
    print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]))

""" I utilized an LLM to help me grasp my idea from the start, and work through my logic and reasoning. It didn't
generate a solution for me, I came up with my solution independently.
"""

""" O(1) is impossible for this alogrithm because in order to find the second distinct value, you must increment through the rows
to find the next distinct value. At worst, the next distinct value could appear as the very last element. The number of  operations 
grows with the number of elements in the matrix. 
"""