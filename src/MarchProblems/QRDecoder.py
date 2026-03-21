# 3/21:

""" Directions: Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.
For example, given:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
or given the same code with a different orientation:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.
"""

""" Time Complexity: O(n^2) -> each rotation rebuilds the rows, meaning for an N x N grid, rotating will take O(n^2).
Each of the N^2 cells are visited once, and even though the maximum rotations is 4, the constant factor doesn't change
the time complexity.
Space Complexity: O(n^2) -> each rotation creates a new N x N matrix, which is O(n^2) space. The binary_data string is storing
all the non-corner cells which is roughly N^2 in memory. The row, column and loop variables are all constant memory.
"""

def decode_qr(qr_code):

    # loop through all four possible rotations
    for _ in range(4):

        # slice the matrix to find the top-left, top-right and bottom-left  corners
        top_left_row1 = qr_code[0][0:2]
        top_left_row2 = qr_code[1][0:2]

        top_right_row1 = qr_code[0][4:6]
        top_right_row2 = qr_code[1][4:6]

        bottom_left_row4 = qr_code[4][0:2]
        bottom_left_row5 = qr_code[5][0:2]

        # print(top_left_row1)
        # print(top_left_row2)
        # print(top_right_row1)
        # print(top_right_row2)
        # print(bottom_left_row4)
        # print(bottom_left_row5)

        # check the corners for the correct orientation
        if (top_left_row1 == '11' and top_left_row2 == '11' and
            top_right_row1 == '11' and top_right_row2 == '11' and
            bottom_left_row4 == '11' and bottom_left_row5 == '11'):
            break

        # if orientation isn't correct, rotate 90 degrees clockwise
        qr_code = [''.join(row) for row in zip(*qr_code[::-1])]

    # initialize to an empty string
    binary_data = ""

    # increment through the rows and columns of the 6x6 matrix, the first if checks the
    # top-left corner, then the top-right corner, and then the bottom-left corner
    for row in range(6):
        for column in range(6):
            if ((row < 2 and column < 2) or
                (row < 2 and column >= 4) or
                (row >= 4 and column < 2)):
                continue

            # concatenate the values at each row and column, excluding the three corners
            binary_data += qr_code[row][column]

    return binary_data

# main test cases
if __name__ == "__main__":
    print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]))
    print(decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]))
    print(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]))
    print(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]))
    print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]))

""" I utilized an LLM to help me work through my original logic and reasoning, and derive a solution
to perform the rotation checks. My original solution at first glance was to "cut-out" the corners from
the original matrix, but I realized looping through each row and column was much easier.
"""

###########################################################################################

"""
ChatGPT's optimal solution: Time and Space are the same for this solution as well

def decode_qr(qr_code):

    # Try all 4 rotations
    for _ in range(4):
        # Check if the QR code is correctly oriented
        if (qr_code[0][0:2] == '11' and qr_code[1][0:2] == '11' and
            qr_code[0][4:6] == '11' and qr_code[1][4:6] == '11' and
            qr_code[4][0:2] == '11' and qr_code[5][0:2] == '11'):
            break
            
        # Rotate 90° clockwise inline
        qr_code = [''.join(row) for row in zip(*qr_code[::-1])]

    # Extract binary data skipping the 3 corner markers
    binary_data = ''.join(
        qr_code[r][c]
        for r in range(6)
        for c in range(6)
        if not ((r < 2 and c < 2) or (r < 2 and c >= 4) or (r >= 4 and c < 2))
    )

    return binary_data
    
"""