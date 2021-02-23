# Asks user for number n and prints the sum of numbers 1 to n.

#Ask user to input number, store in variable n.
n = input('Choose a number: ')

#Store number as an integer.
n = int(n)

#Create a list of numbers from 1 to n.
listn = list(range(1, n+1))

#Add numbers in the list, store in variable sumn
sumn = sum(listn)

#Display result to user.
print(sumn)





