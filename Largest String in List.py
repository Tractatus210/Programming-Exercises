# Write a function that returns the largest element in a list.

# Largest string in a list of strings.

list = ['apple', 'banana', 'potato', 'aubergine', 'chicken']

def listOrder(list):
    # Use sorted instead of sort to create a new list, leaving the original intact. Add length key.
    sortedList = sorted(list, key=len)
    print(sortedList[0])

listOrder(list)
