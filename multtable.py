# Write a program that prints a multiplication table for numbers up to 12.

# Define a function multiplies number a by 1, ..., 12 and adds result to a list at each iteration.
# a iterates from 1 to 12.
def multSeq(b):
    # Create empty list.
    multList = []
    # Set a as 1 for default value.
    a = 1
    # Create loop that multiplies number b by 1 to 12.
    while a <= 12:
        # Create variable to hold each step of multiplication sequence.
        mult = a*b
        # Add result to list.
        multList.append(mult)
        # Add 1 to a to multuply b by next number.
        a += 1
    #print the list of a*b for values of a from 1 to 12.
    print(multList)

# Define a function that repeats the multiSeq function with values of b from 1 to 12.
def multiIter():
    # Set b as 1 for default value
    b = 1
    # Create loop to iterate for values of b up to 12.
    while b <= 12:
        # Perform the multiplication function for the value of b.
        multSeq(b)
        # Increase the value of b by 1 to create the next multiplication table.
        b +=1

# Perform multiIter function to obtain multiplication tables for number 1 to 12.

multiIter()











