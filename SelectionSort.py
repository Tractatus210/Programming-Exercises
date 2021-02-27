# Selection Sort

def selSort(li):
    # Variable i iterates through each element of the list from index 0 to the end.
    for i in range(0, len(li)):
    # As a default, the value of i is set as the minimum value index in the list.
        min = i
    # Variable n iterates through each element that follows index[i], up to the end of the list.
        for n in range(i+1, len(li)):
    # If, for any step in the iteration, the value of index[n] is below that is index[min],
    # index[min] is set as the minimum value.
            if li[n] < li[min]:
                min = n
    # Index[i] and index[min] are swapped whenever line 13 places li[min] after li[i] in the list.
        li[i], li[min] = li[min], li[i]
    print(li)

# Same as above but the original list is kept intact and a new, sorted list is produced.
# Outputs both lists for comparison.

def selSortKeep(li):
    sortedList = []
    for a in range(0, len(li)):
        sortedList.append(li[a])
    for i in range(0, len(sortedList)):
        min = i
        for n in range(i+1, len(sortedList)):
            if sortedList[n] < sortedList[min]:
                min = n
        sortedList[i], sortedList[min] = sortedList[min], sortedList[i]


    print('The original list is ' + str(li))
    print('The sorted list is ' + str(sortedList))
