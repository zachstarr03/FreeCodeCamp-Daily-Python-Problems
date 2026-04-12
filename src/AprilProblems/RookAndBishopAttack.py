# 4/11:

""" Directions: Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one piece can attack another.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1

Rooks can move as many squares as they want in a horizontal or vertical direction.
Bishops can move as many squares as they want in any diagonal direction.
One piece can attack another if it can move to the location of that piece.
Return:

"rook" if the rook can attack the bishop.
"bishop" if the bishop can attack the rook.
"neither" if neither piece can attack one another.
"""

""" Time Complexity: O(1) -> The input is always of a fixed-size, therefore the input is never growing so time is constant.
All operations are of constant time as well.
Space Complexity: O(1) -> With the input being a fixed-size, memory is constant regardless of the input. All variables are stored
in constant space and there are no extra data structures that grow with the input.
"""

def rook_bishop_attack(rook, bishop):

    # Slicing to get the column and row for the rook's location
    rook_column = rook[:1]
    rook_row = int(rook[1:])

    # Slicing to get the column and row for the bishop's location
    bishop_column = bishop[:1]
    bishop_row = int(bishop[1:])

    # Convert the columns into ASCII integer values (A: 0 - G: 7)
    rook_column_num = ord(rook_column) - ord('A')
    bishop_column_num = ord(bishop_column) - ord('A')

    # print(rook_column_num)
    # print(bishop_column_num)

    # if either the rook's column or row is equal to the bishop's column or row, the rook can capture
    if rook_column == bishop_column or rook_row == bishop_row:
        return "rook"

    # handles all four different diagonal movements the bishop can perform to capture the rook
    elif abs(rook_column_num - bishop_column_num) == abs(rook_row - bishop_row):
        return "bishop"

    # return 'neither' if neither the rook or bishop can perform a capture
    else:
        return "neither"

# main test cases
if __name__ == "__main__":
    print(rook_bishop_attack("A1", "A5"))
    print(rook_bishop_attack("C3", "F6"))
    print(rook_bishop_attack("D4", "D7"))
    print(rook_bishop_attack("B7", "H1"))
    print(rook_bishop_attack("B3", "C5"))
    print(rook_bishop_attack("G3", "E8"))

""" I did not utilize an LLM at all while working through my solution. """

########################################################################################################

"""
ChatGPT's optimal solution (cleaner and more readable): time and space are the same

def rook_bishop_attack(rook, bishop):
    dx = abs((ord(rook[0]) - ord('A')) - (ord(bishop[0]) - ord('A')))
    dy = abs(int(rook[1]) - int(bishop[1]))

    if dx == 0 or dy == 0:
        return "rook"
    if dx == dy:
        return "bishop"
    return "neither"
"""