# 3/28:

""" Directions: Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

Here's the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

""" Time Complexity: O(n^2) -> Incrementing through the rows to reach the nth row is O(n), followed by another
loop to increment through the nth row and append values. The length of row is growing each time so n(n - 1)/2 
gives you O(n^2) when simplified.
Space Complexity: O(n) -> One row at a time is being built, not the entire triangle, therefore space grows linearly with
the input. Storing all the rows would cause space to be O(n^2).
"""

def pascal_row(n):

    # check for the first 1
    if n == 1:
        return [1]

    # build the rows off of the first row
    row = [1]

    # increment through the nth rows, set the current row to have a 1 before building the middle
    # values, and then increment through the range of the row (row 1) appending the middle values
    for _ in range(n - 1):
        current_row = [1]
        for value in range(len(row) - 1):
            current_row.append(row[value] + row[value + 1])

        # append a 1 to the end to finish the row, and set row equal to current row
        current_row.append(1)
        row = current_row

    return row

# main test cases
if __name__ == "__main__":
    print(pascal_row(5))
    print(pascal_row(3))
    print(pascal_row(1))
    print(pascal_row(10))
    print(pascal_row(15))

""" I utilized an LLM at first to check if I was on the right path with my reasoning at logic at the start. From there,
I built upon my code and came up with a viable solution.
"""

#######################################################################################################################

"""
ChatGPT's optimal solution: time complexity is O(n) now by optimizing it to use the relationship between consecutive 
binomial coefficients, but space is the same

    def pascal_row(n):
    row = [1]
    
    for k in range(1, n):
        next_val = row[-1] * (n - k) // k
        row.append(next_val)
    
    return row
"""