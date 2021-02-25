# Write three functions that compute the sum of the numbers in a list:
# using a for-loop, a while-loop and recursion.

# For loop

def forSum(a):
    total = 0
    for n in a:
        total = total + n
    print(total)

# While Loop

def whileSum(a):
    n = 0
    total = 0
    while n < len(a):
        total = total + a[n]
        n += 1
    print(total)

# Recursion

def recurSum(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + recurSum(a[1:])














