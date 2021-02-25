# Write a function that tests whether a string is a palindrome.

def isPalindrome(a):
# Reverse string and store in variable.
    b = a[::-1]
# Check if variables have the same value and output accordingly.
    if a == b:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')




