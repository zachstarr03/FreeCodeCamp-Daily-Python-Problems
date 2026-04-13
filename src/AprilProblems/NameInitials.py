# 4/13:

""" Directions: Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".
"""

""" Time Complexity: O(n) -> as the length of the input string grows, time grows linearly since the for loop must iterate
over each word in the input.
Space Complexity: O(n) -> performing a split on the input stores all the words in a list, and I initialized a list to
store all the initials, which are both O(n) space operations.  
"""

def get_initials(name):

    # split the name by the spaces, to retrieve the first initial of each word
    name_split = name.split(" ")

    # empty list to append the initials to
    initials_list = []

    # increment through the list of words, get the first initial of each word, and append each initial to the empty list
    for index, word in enumerate(name_split):
        initials = word[:1]
        # print(initials)
        initials_list.append(initials)

    # print(initials_list)

    # join the initials together separated by a '.' and concatenate a '.' at the end too
    return ".".join(initials_list) + '.'

# main test cases
if __name__ == "__main__":
    print(get_initials("Tommy Millwood"))
    print(get_initials("Savanna Puddlesplash"))
    print(get_initials("Frances Cowell Conrad"))
    print(get_initials("Dragon"))
    print(get_initials("Dorothy Vera Clump Haverstock Norris"))

""" I did not utilize an LLM at all while deriving my solution. """

########################################################################################################################

""" ChatGPT's optimal solution (cleaner and minimal extra space): time is still O(n), but space is now O(1)

def get_initials(name):
    result = []
    new_word = True

    for char in name:
        if char == " ":
            new_word = True
        elif new_word:
            result.append(char.upper())
            new_word = False

    return ".".join(result) + "."
"""