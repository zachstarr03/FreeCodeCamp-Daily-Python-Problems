# 3/24:

""" Directions: Given an array of student exam scores and the score needed to pass it,
return the number of students that passed the exam.
"""

""" Time Complexity: O(n) -> you must always increment through the entire scores array, so as input n grows, time
complexity grows linearly.
Space Complexity: O(1) -> no operations use extra memory, and no data structures are utilized, therefore space
is constant.
"""

def passing_count(scores, passing_score):

    # initialize a variable to keep count of students who passed
    total_passing_students = 0

    # increment through the scores array, if a value is greater or equal
    # to the passing_score value add a student to the total_passing_students count
    for score in scores:
        if score >= passing_score:
            total_passing_students += 1

    return total_passing_students

# main test cases
if __name__ == "__main__":
    print(passing_count([90, 85, 75, 60, 50], 70))
    print(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75))
    print(passing_count([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60))
    print(passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85))
    print(passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60))

""" I did not utilize an LLM for this problem at all, all the work above is my own reasoning
and logic. 
"""