# 3/01:

""" Directions: Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.
"""

""" Time Complexity: scales linearly with the length of the list 
Best case: O(1) -> if the first element is a list (early return) 
Worst case: O(n) -> if the array is flat or the list is at the end -> Big-O represents worst case

Space Complexity: simple loop variable (i) -> constant space 
No additional data structures or the creation of new lists or copies
"""

''' O(n) time complexity, O(1) space complexity '''
def is_flat(arr):

    # increment through the arr, if a nested list is found return False right away,
    # otherwise keep incrementing and return True if no nested list
    for i in range(len(arr)):
        #print(f"Index {i}: {arr[i]}")
        if (type(arr[i]) == list):
            return False

    return True

if __name__ == "__main__":
    print(is_flat([1, 2, 3, 4]))
    print(is_flat([1, [2, 3], 4]))
    print(is_flat(["a", [0], "b", True]))
    print(is_flat([1, [2, [3, [4, [5]]]], 6]))

''' Once again, an LLM helped me understand my reasoning and logic, and I was able to derive a fully functioning solution on my own, without it giving me the full correct solution '''
