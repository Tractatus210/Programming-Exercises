# Write a function that computes the running total of a list.

def runningTotal(a):
    # Make blank list b to capture values in a.
    b = []
    # Iterate through elements of a one by one, showing running total.
    for i in a:
        b.append(i)
        print(sum(b))
