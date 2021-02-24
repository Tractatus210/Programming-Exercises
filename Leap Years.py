# Write a program that prints the next 20 leap years.

import datetime

# Store current year in variable.
year = datetime.date.today().year

leapYears = []
while len(leapYears) < 20:
    year += 1
    # Check that year is divisible by 4.
    yearMod = year % 4
    if yearMod == 0:
        #If year is divisible by 4 and 100, check that it is divisible by 400.
        centMod = year % 100
        if centMod == 0:
            fCentMod = year % 400
            if fCentMod == 0:
                leapYears.append(year)
        else:
            leapYears.append(year)
print(leapYears)






