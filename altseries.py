# Write a program that computes the sum of an alternating series
# where each element of the series is an expression of the form ((-1)^{k+1})/(2 * k-1)
# for each value of kk from 1 to a million, multiplied by 4.

# Define function with equation, with k as an argument.
def altSer(k):
    # The first iteration involves a multiplication by 0. Create exception to avoid error.
    try:
        val = ((-1) ** (k + 1)) / (2 * (k - 1)) * 4
    except ZeroDivisionError:
        val = float('inf')
    print(float(val))

k = 1

# Pass values of k through function within specified range.
for k in range (1, 1000001):
    altSer(k)






