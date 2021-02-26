# Write a function that takes a number and returns a list of its digits.
# So for 2342 it should return [2,3,4,2].

def numList(n):
    # empty list to store digits.
    liNum = []
    # convert number to string and iterate through each character.
    for a in str(n):
        # convert each character back to an integer and append to list.
        liNum.append(int(a))
    print(liNum)


