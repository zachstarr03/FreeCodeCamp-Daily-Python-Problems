# 3/10:

""" Directions: Given an array, a value to insert into the array, and an index to insert
 the value at, return a new array with the value inserted at the specified index.
"""

""" Method 1:
Time Complexity: O(n) -> lists are dynamic arrays, therefore when insertiing at an index every element after that index is shifted one position to the right.
An array with n elements can lead to n elements that might need to be shifted.
Space Complexity: O(1) -> modifiying the original list does not create any additional space (in-place modification) 

Method 2:
Time Complexity: O(n) -> slicing copies part of the array which is up to O(n) time, and then  concatenates the value to create a new list
Space Complexity: O(n) -> because a new array is being created, space complexity is now O(n)
"""
def insert_into_array(arr, value, index):

    # method 1: .insert() works, but modifies the original list

    # index: position in the list where the new element will be added
    # value: the new element being added
    # arr.insert(index, value)

    # method 2: slicing (does not modify the original list)

    # arr[:index]: part of the list before the specified index, [value]: inserts the new element, arr[index:] rest of the list after the specified index
    new_arr = arr[:index] + [value] + arr[index:]

    return new_arr

# main test cases
if __name__ == "__main__":
    print(insert_into_array([2, 4, 8, 10], 6, 2))
    print(insert_into_array(["the", "quick", "fox"], "brown", 2))
    print(insert_into_array([], 0, 0))
    print(insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5))

''' .append() would work when adding an element only at the end of the list, so you could have logic that checks
if index == len(arr), then use arr.append(value), else use arr.insert(index, value). .append() is more efficient,
since all subsequent elements don't need to be shifted.
'''