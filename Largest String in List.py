# Write a function that returns the largest element in a list.

# Largest string in a list of strings.

def listOrder(list):
    # Use sorted instead of sort to create a new list, leaving the original intact.
    # Add length key. Set reverse to True to display largest value first.
    sortedList = sorted(list, key=len, reverse=True)
    print(sortedList[0])
