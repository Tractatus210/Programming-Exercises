# Write a program that prints all prime numbers.

# Create a function to establish if a number is prime.
def isPrime(n):
    d = 1
    modN = 0
    while d <= n:
        mod = n % d
        if mod >= 1:
            modN += 1
        d += 1
    if modN == n-2:
        print(n)


# While loop to run infinite increments of n through the isPrime function.

n = 1
while True:
    isPrime(n)
    n += 1



