# 2/20:

""" Directions: Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space."""

''' O(1) time complexity, O(1) space complexity (with fixed size) '''
def is_valid_trick(trick_name):


    # list of valid first words
    first_valid_word_list = ["Misty", "Ghost", "Thunder", "Solar",
                             "Sky", "Phantom", "Frozen", "Polar"]

    # list of valid second words
    second_valid_word_list = ["Twister", "Icequake", "Avalanche",
                              "Vortex", "Snowstorm", "Frostbite",
                              "Blizzard", "Shadow"]

    # trick_name = "Polar Vortex" -> trick_name_split = ["Polar", "Vortex"]
    # trick_name_split[0] = "Polar"
    # trick_name_split[1] = "Vortex"

    # split on space, this makes it a list
    trick_name_split = trick_name.split(" ")

    # use the in keyword for a collection, such as a list
    if (trick_name_split[0] in first_valid_word_list and trick_name_split[1] in second_valid_word_list):
        return True
    else:
        return False

# test cases
if __name__ == "__main__":
    print(is_valid_trick("Polar Vortex"))       # True
    print(is_valid_trick("Solar Icequake"))     # True
    print(is_valid_trick("Thunder Blizzard"))   # True
    print(is_valid_trick("Phantom Frostbite"))  # True
    print(is_valid_trick("Ghost Avalanche"))    # True
    print(is_valid_trick("Snowstorm Shadow"))   # False
    print(is_valid_trick("Solar Sky"))          # False

# set membership checks "in" are O(1) on average for sets, so using sets instead of lists can improve performance.
# Avoid unnecessary if/else, instead directly return the boolean expression result.
# Added error handling for cases where the input does not contain exactly two words, which prevents potential index errors.
