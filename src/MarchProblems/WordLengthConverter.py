# 3/11:

""" Directions: Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.

For example, given "hello world", return "5 5".
"""

""" Time Complexity: O(n) -> each operation is O(n) times as they each grow linearly as the length of the input string grows 
Split: must look at each character to find the spaces -> O(n)
Loop: counting each character across each word -> sum of all word lengths = n -> O(n)
Convert and append: scanning over n words means n characters to convert and append -> O(n)
Join: creates a new string with each character of n size -> O(n)

Space Complexity: O(n) -> each operation is once again O(n) times 
Split: creates a list of words, where the space is proportional to the number of characters -> O(n)
List of lengths: one word is one string, total characters of that string = n -> O(n)
Join: creates a new string of length n -> O(n)
"""

def convert_words(s):

    # split each word on the space and create an empty list to store the lengths of each word later
    words = s.split(" ")
    lengths = []

    # increment through the list of words split on the space, find the length of each one,
    # append each length to the lengths list, and use .join() to convert the list into a string
    # separated with spaces
    for word in words:
        word_length = len(word)
        lengths.append(str(word_length))
        word_length_s = " ".join(lengths)

    return word_length_s

# main test cases
if __name__ == "__main__":
    print(convert_words("hello world"))
    print(convert_words("Thanks and happy coding"))
    print(convert_words("The quick brown fox jumps over the lazy dog"))
    print(convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"))

''' An LLM helped me reason through my logic and understand the core principle behind creating a list to solve this problem.
It did not write this solution, I wrote everything myself and utilized an LLM to help me conceptually visualize the path forward.
'''

''' At first glance, I wanted to try and using the .replace() and once I worked through the problem,
I realized this method manipulates the original string, which is slower and also harder to understand.
If a word ends up repeating itself, then all instances will get replaced at once, which might lead to some
issues later on. Creating a list to store the lengths, looping through the .split(), and using a .join()
is cleaner and safer. 
'''
