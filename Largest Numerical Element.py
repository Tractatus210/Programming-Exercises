# Write a function that returns the largest element in a list.

#Largest integer in a list of integers.

def listOrder(list):
    # Use sorted instead of sort to create a new list, leaving the original intact.
    # Set reverse to True to display largest value first.
    sortedList = sorted(list, reverse=True)
    print(sortedList[0])



