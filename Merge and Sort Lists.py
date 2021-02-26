# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# You can do this quicker than concatenating them followed by a sort.

def sortList(a, b):
    # Create variable to store concatenated list. Output the value of this variable.
    c = a + b
    # Sort this list.
    c.sort()
    print(c)


