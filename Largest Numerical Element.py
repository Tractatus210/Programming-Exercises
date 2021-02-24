# Write a function that returns the largest element in a list.

#Largest integer in a list of integers.

list = [5, 1, 3, 2, 7]

def listOrder(list):
    # Use sorted instead of sort to create a new list, leaving the original intact.
    sortedList = sorted(list)
    print(sortedList[0])

listOrder(list)

