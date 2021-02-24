# Write a function that returns the elements on odd positions in a list.

# Define function with placeholder argument for list.
def listOdd(a):
    # Standard for loop to iterate through list elements.
    for n in range(len(a)):
        # Add exception for even numbers.
        if n % 2 == 0:
            print(a[n])

