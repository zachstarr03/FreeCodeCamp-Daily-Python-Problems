# 4/10:

""" Directions: Given two strings for the location of two rooks on a chess board, determine if they can attack each other.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1

Rooks can move as many squares as they want in a horizontal or vertical direction. So if they are on the same row or column, they can attack each other.
"""

""" Time Complexity: O(1) -> The two input strings are always of a fixed-size, therefore time is constant.
The amount of work the program needs to perform will never grow with the input size.
Space Complexity: O(1) -> Space does not grow as the input grows, since the input are of fixed-size. There are
no data structures utilized or extra memory operations.
"""

def rook_attack(rook1, rook2):

    # Slice the rook1's string to get its location (column and row)
    rook1_column = rook1[:1]
    rook1_row = rook1[1:]

    # Slice the rook2's string to get its location (column and row)
    rook2_column = rook2[:1]
    rook2_row = rook2[1:]

    # Comparison to see if either the two columns or rows are equal, if so the two rooks can attack each other
    if rook1_column == rook2_column or rook1_row == rook2_row:
        return True
    else:
        return False

# main test cases
if __name__ == "__main__":
    print(rook_attack("A1", "A8"))   # True
    print(rook_attack("B4", "F4"))   # True
    print(rook_attack("E3", "D4"))   # False
    print(rook_attack("H7", "F6"))   # False

""" I did not use an LLM at all while working through my solution. """

###################################################################################################################

"""
ChatGPT's optimal solution (avoids extra variables, more efficient): time and space remain the same

def rook_attack(rook1, rook2):
    return rook1[0] == rook2[0] or rook1[1] == rook2[1]
"""