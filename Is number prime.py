# Write a program that checks if n is a prime number.


# Request dividend n as input.
n = input('Enter a number to see if it\'s prime: ')
n = int(n)
# Set default value of divisor d as 1.
d = 1

# Create variable to count cases in which n does not divide by d, set default value as 0.
modN = 0

# While loop to operate for all values of d up to n.
while d <= n:
    # Establish modulus of n and d and capture in variable.
    mod = n % d
    # Increment modN by 1 if there is a remainder.
    if mod >= 1:
        modN += 1
    # Increment d by 1.
    d += 1

# If all divisions of n/d, except when d=1 and d=n, produce a remainder, n is prime.

if modN == n-2:
    print ('%d is prime' %n)
else:
    print ('%d is not prime' %n)
