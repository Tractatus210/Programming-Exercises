# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

sec = 35

# Make active variable True to determine when loop operates.
active = True

# Create blank list of guesses.
guessList = []

# Create loop that continues unless active variable is false.
while active is True:
    guess = input('Guess the number: ')
    guess = int(guess)
    if guess < sec:
        print ('Too low!')
        # Add guess to list of guesses.
        guessList.append(guess)
    elif guess > sec:
        print ('Too high!')
        guessList.append(guess)
    else:
        print ('Good job!')
        guessList.append(guess)
        # Remove duplicates from list of guesses.
        totalGuess = list(set(guessList))
        # Print number of tries.
        if len(guessList) == 1:
            print('You needed %d guess to get the right number.' % len(totalGuess))
        else:
            print('You needed %d guesses to get the right number.' % len(totalGuess))
        # Make the active variable False to end loop.
        active = False



