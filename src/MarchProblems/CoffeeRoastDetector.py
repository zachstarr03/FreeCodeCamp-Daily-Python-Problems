# 3/22:

""" Directions: Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.

The given string will contain the following characters, each representing a type of bean:

An apostrophe (') is a light roast bean worth 1 point each.
A dash (-) is a medium roast bean worth 2 points each.
A period (.) is a dark roast bean worth 3 points each.
The roast level is determined by the average of all the beans.

Return:

"Light" if the average is less than 1.75.
"Medium" if the average is 1.75 to 2.5.
"Dark" if the average is greater than 2.5.
"""

""" Time Complexity: O(n) -> as the input grows, runtime grows linearly. The entire string must be traversed once
and a comparison and addition are performed at each character.
Space Complexity: O(1) -> Only a fixed number of variables are utilized and no additional data structures are present
that grow with the size of the input. A constant amount of extra space is used regardless of input size.
"""

def detect_roast(beans):

    # initialize a total points variable to 0
    total_points = 0

    # increment through the string, an apostrophe is worth 1 point, a dash 2 points, and
    # a period is 3 points each
    for char in beans:
        if char == "'":
            total_points += 1

        elif char == "-":
            total_points += 2

        else:
            total_points += 3

    # print(f"{apostrophe_count}, {dash_count}, {period_count}")

    # calculate the average of all the beans to determine the roast level
    average_roast = total_points / len(beans)
    # print(average_roast)

    # the roast level is "Light" if less than 1.75
    if average_roast < 1.75:
        return "Light"

    # "Medium" if the average is 1.75 to 2.5
    elif average_roast >= 1.75 and average_roast <= 2.5:
        return "Medium"

    # "Dark" if the average is greater than 2.5
    else:
        return "Dark"

# main test cases
if __name__ == "__main__":
    print(detect_roast("''-''''''-'-''--''''"))     # Light
    print(detect_roast(".'-''-''..'''.-.-''-"))     # Medium
    print(detect_roast("--.''--'-''.--..-.--"))     # Medium
    print(detect_roast("-...'-......-..-...-"))     # Dark
    print(detect_roast(".--.-..-......----.'"))     # Medium
    print(detect_roast("..-..-..-..-....-.-."))     # Dark
    print(detect_roast("-'-''''''..-'.''-'.'"))     # Light

""" I did not use an LLM to help me throughout this problem. Once I derived and worked through my solution on my own,
I determined the time and space complexity myself, and then asked ChatGPT to derive an optimal solution to this problem.
"""

#########################################################################################################################

""" 
ChatGPT's optimal solution: time and space complexity are the same

def detect_roast(beans):

    values = {"'": 1, "-": 2, ".": 3}
    total = sum(values[c] for c in beans)
    avg = total / len(beans)

    if avg < 1.75:
        return "Light"
    elif avg <= 2.5:
        return "Medium"
    return "Dark"
"""

""" Representing the values as a dictionary is a very clean Pythonic version solution. I did think of creating
a dictionary at first, but instead I just went through different reasoning and logic.
"""