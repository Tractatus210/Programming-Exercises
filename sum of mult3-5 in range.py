# Asks user for number n and prints the sum of all multiples of 3 and 5 in the range of 1 to n.

#Ask user to input number, store in variable n.
n = input('Choose a number: ')

#Convert n to integer.
n = int(n)

#Create a list of all multiples of 3 between 1 and n.
list1 = list(range(0, n+1, 3))
#list1 starts at 0 and increments by 3, 0 will not affect the final sum.

#Create a list of all multiples of 5 between 1 and n.
list2 = list(range(0, n+1, 5))
#list2 again starts at 0; this will not influence the final sum.

#Add list1 and list2.
list3 = list1 + list2

#Remove duplicates from list3.
list4 = list(set(list3))

#Add numbers in list4.
sum4 = sum(list4)

#Display result to user.
print(sum4)




