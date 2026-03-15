# 3/15:

""" Directions: Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	    "P"	            8	      1
Rook	    "R"	            2	      5
Knight	    "N"	            2	      3
Bishop	    "B"	            2	      3
Queen	    "Q"	            1	      9
King	    "K"	            1	      0

The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".
"""

""" Time Complexity: O(n) -> the input array of pieces has n pieces, therefore the loop runs n times. Time grows linearly with input size.
Space Complexity: O(1) -> the dictionary will always contain 6 elements (6 chess pieces), no matter the input size. Size does not grow with
n, and all the variables are constant memory; memory is not allocated proportional to n. The only extra memory is constant.
"""

def get_captured_value(pieces):

    # (8 * 1) + (2 * 5) + (2 * 3) + (2 * 3) + (1 * 9)
    total_value = 39

    piece_values = {
                    "P": 1, "R": 5, "N": 3,
                    "B": 3, "Q": 9, "K": 0
                   }

    # return "Checkmate" if the King is not present (King has been captured)
    if "K" not in pieces:
        return "Checkmate"

    # variable to store the value of pieces still on the board
    uncaptured_value = 0

    # increment through the pieces array to determine the value of pieces not captured
    for piece in pieces:
        # print(piece_values[piece])
        uncaptured_value += piece_values[piece]

    # calculate the value of pieces the opponent has captured
    captured_value = total_value - uncaptured_value

    return captured_value

# main test cases
if __name__ == "__main__":
    print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))                         # 8
    print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))                                             # 26
    print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]))                         # 16
    print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]))               # 4
    print(get_captured_value(["P", "K"]))                                                                           # 38
    print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]))     # 0
    print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]))                              # Checkmate

''' The maximum value of n is <= 16, since in chess there are only 16 pieces, meaning the runtime is technically constant; but when you 
analysis an algorithm you're concerned about the input length, therefore time complexity is O(n).
'''