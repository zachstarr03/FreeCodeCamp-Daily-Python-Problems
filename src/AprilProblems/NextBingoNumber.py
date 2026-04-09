# 4/09:

""" Directions: Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
 "B"	   1-15
 "I"	   16-30
 "N"	   31-45
 "G"	   46-60
 "O"	   61-75

For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".
"""

""" Time Complexity: O(1) -> The input is of fixed size, so time complexity does not grow with input size. The
letters list is of fixed size as well. All operations are O(1).
Space Complexity: O(1) -> Space doesn't grow with input either, even though I used a dictionary and a list both
of their sizes are fixed and independent of the input.
"""

def get_next_bingo_number(n):

    # dictionary to sort the bingo letter as the key with the values being the number range
    bingo_number = {'B': (1, 15),
                    'I': (16, 30),
                    'N': (31, 45),
                    'G': (46, 60),
                    'O': (61, 75)
                   }

    # list to store all the letters
    letters = ['B', 'I', 'N', 'G', 'O']

    # slice the letter and number value from the input n
    letter = n[0]
    number = int(n[1:])

    # print(letter)
    # print(number)

    # determine the min and max value
    min_value, max_value = bingo_number[letter]

    # if the number sliced + 1 is greater than the max in that letter's range, wrap around
    # to the next letter and use its value at index 0 for the new value, else just increment
    # number
    if number + 1 > max_value:
        letter_index = letters.index(letter)
        letter_index = (letter_index + 1) % len(letters)
        letter = letters[letter_index]
        number = bingo_number[letter][0]
    else:
        number += 1

    # format the next bingo number with the letter (new if wrapping occurs), and the new number
    next_n = f"{letter}{number}"

    return next_n

# main test cases
if __name__ == '__main__':
    print(get_next_bingo_number("B10"))
    print(get_next_bingo_number("N33"))
    print(get_next_bingo_number("I30"))
    print(get_next_bingo_number("G60"))
    print(get_next_bingo_number("O75"))

""" I utilized an LLM to make sure my approach was on track and my logic was good. I didn't use it to generate
a solution.
"""

################################################################################################################

"""
ChatGPT's optimal solution (faster and more memory-efficient): time and space are the same
 
def get_next_bingo_number(n):
    number = int(n[1:])          # parse number
    number = number % 75 + 1      # increment and wrap after 75
    letters = ['B', 'I', 'N', 'G', 'O']
    letter = letters[(number - 1) // 15]  # determine letter from number
    return f"{letter}{number}
"""