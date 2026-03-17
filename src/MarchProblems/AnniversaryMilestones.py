""" Directions Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
     1	         "Paper"
     5	         "Wood"
     10	         "Tin"
     25	         "Silver"
     40	         "Ruby"
     50	         "Gold"
     60	         "Diamond"
     70	         "Platinum"

If they haven't reached the first milestone, return "Newlyweds".
"""

""" Time Complexity: O(1) -> the algorithm is only checking up to 8 milestones, which is the fixed size of the sorted list,
meaning the time complexity is constant time. The number of iterations only depends on the length of milestone_years, not years.
Space Complexity: O(1) -> the dictionary contains 8 key-value pairs of fixed size, and the sorted list also contains 8 elements
of fixed size. No structures are growing with the input, the variables are just references, so space is constant.
"""

def get_milestone(years):

    # dictionary which stores the years married as the key and the milestone name as the value
    anniversary = {
                    1: "Paper", 5: "Wood", 10: "Tin", 25: "Silver",
                    40: "Ruby", 50: "Gold", 60: "Diamond", 70: "Platinum"
                  }

    # sorted list of years married to get the key for the dictionary
    milestone_years = [1, 5, 10, 25, 40, 50, 60, 70]

    # assign the current milestone to "Newlyweds"
    current_milestone = "Newlyweds"

    # increment through the sorted years married list, if the year is less than or equal to the input,
    # set the current milestone to the value of that year inside the dictionary -> O(1) lookup for a dictionary.
    # the else allows the loop to break, so iterations don't go all the way until the end of the sorted list for
    # any given input. It is explicitly shown to also help showcase the logic completely and to follow easier.
    for year in milestone_years:
        if year <= years:
            current_milestone = anniversary[year]
        else:
            break

    return current_milestone

# main test cases
if __name__ == "__main__":
    print(get_milestone(0))
    print(get_milestone(1))
    print(get_milestone(8))
    print(get_milestone(10))
    print(get_milestone(26))
    print(get_milestone(45))
    print(get_milestone(50))
    print(get_milestone(64))
    print(get_milestone(71))

""" I used an LLM to briefly help me with my reasoning and logic, and to see if I was on the correct path. It did not
give me a full solution or generate my solution at all.
"""

######################################################################################################################

"""
ChatGPT"s optimal solution is below: time and space complexity are both still O(1)

def get_milestone(years):
    anniversary = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    current_milestone = "Newlyweds"

    # Iterate over the keys in ascending order
    for year in sorted(anniversary.keys()):
        if year > years:
            break
        current_milestone = anniversary[year]

    return current_milestone
"""