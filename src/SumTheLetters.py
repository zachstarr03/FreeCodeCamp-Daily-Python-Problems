# 3/02:

""" Directions: Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.
"""

""" Time Complexity: scales linearly with the length of the string
Creating the dictionary: O(1) -> always has 26 fixed entries, size doesn't depend on input size
Converting the string to lowercase: O(n) -> must process each character once, takes time proportional to the string length
Looping through the string: O(n) -> Dictionary membership check: O(1) average case, Dictionary lookup: O(1), Addition: O(1)
O(1) + O(n) + O(n) = O(n)

Space Complexity: extra space due to creating a new string with lower_s, could reduce to O(1) if done on the fly
dictionary space: O(1) -> fixed size of 26 key-value pairs, independent of input size
lower_s: O(n) -> creates a new string, same length as s
word_sum: O(1) and char: O(1) -> simple variables, constant space
O(1) + O(n) = O(n)
"""

''' O(n) time complexity, O(n) space complexity '''
def sum_letters(s):

    letter_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }

    # Normalize the string and initialize word_sum
    lower_s = s.lower()
    word_sum = 0

    # iterate through the string (accepts only letters), check if each char is in the letter_dict, if so add its value to the sum
    for char in lower_s:
        if char in letter_dict:
            word_sum += letter_dict[char]

    return word_sum

if __name__ == "__main__":
    print(sum_letters("hello"))
    print(sum_letters("freeCodeCamp"))
    print(sum_letters("The quick brown fox jumps over the lazy dog."))
    print(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, "
          "pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in "
          "faucibus orci."))
    print(sum_letters("</404>"))

''' Once again, an LLM helped me understand my reasoning and logic, and I was able to derive a fully functioning solution on my own, without it giving me the full correct solution '''
