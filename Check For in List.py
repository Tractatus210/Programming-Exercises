# Write a function that checks whether an element occurs in a list.

# Checks whether a can be found in b and returns the result.
def checkFor(a, b):
    if a in b:
        print('Yes, %s is in the list.' % a)
    else:
        print('No, %s is not in the list.' % a)

