# Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.

def on_all():
    # Create blank lists a and b.
    a = []
    b = []
    # Fill a and b with numbers 1 to 20.
    n = 1
    while n <= 20:
        a.append(n)
        b.append(n)
        n += 1
    # Define a function to multiply each element of a by the corresponding element of b.
    def calcSq(i):
        print(a[i] * b[i])
    # Call function with arguments iterating through each index of a and b.
    for i in range(0, len(a)):
        calcSq(i)
