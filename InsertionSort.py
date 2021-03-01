# Insertion Sort

def inserSort(l):
    for i in range(1, len(l)):
        current = l[i]
        previous = l[i-1]
        while i > 0 and previous > current:
            l[i-1], l[i] = l[i], l[i-1]
            i -= 1
            current = l[i]
            previous = l[i-1]
    print(l)


