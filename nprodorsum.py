# Write a program that asks the user for a number n and gives them the possibility to choose between
# computing the sum and computing the product of 1, ..., n.


#Ask user to input number, store as variable n.
n = input('Enter a number: ')

#Convert n to integer.
n = int(n)

#Create a list of numbers 1 to n.

listNum = list(range(1, n+1))

#Define a function to add numbers in listNum.
def sumFunc():
    #Add numbers in listNum, store in sumN.
    sumN = sum(listNum)
    #Display sum
    print(sumN)

#Define a function to multiply numbers in listNum.
def multiFunc():
    #Create a for loop to multiply numbers in listNum.
    # multN starts as 1 to avoid result of 0.
    multN = 1
    # x will iterate through each number in the list.
    for x in listNum:
        # Store product in multN.
        multN *= x
    #display product
    print(multN)

# Define a function to ask user to press 1 to choose sum or press 2 to choose product.
def choice():
    # Store answer in variable.
    ans = input('Enter 1 to see the sum of all numbers from 1 to your number, \nor enter 2 for the product of these numbers: ')
    # If user has has chosen 1, start the sum function.
    if ans == '1':
        sumFunc()
    # If user has chosen 2, start the multiply function.
    elif ans == '2':
        multiFunc()
    # If the user has chosen neither, restart the choice function to ask user to choose again.
    else:
        choice()

choice()




