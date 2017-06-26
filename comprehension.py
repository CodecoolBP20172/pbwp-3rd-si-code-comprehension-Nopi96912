# This program is a Guess a Number game
import random  # Import module 'random'

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # Print a string
myName = input()  # Assign the input to myName variable

number = random.randint(1, 20)  # Assign a number between 1 and 20 to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Print string with the myName
# variable inside it

while guessesTaken < 6:  # Execute the code under it while guessesTaken variable don't reach 6
    print('Take a guess.')  # Print a string
    guess = input()  # Assign the input to guess variable
    guess = int(guess)  # Change the guess variable to an integer

    guessesTaken += 1  # Add 1 to the guessesTaken variable

    if guess < number:  # See that guess variable is lower than number variable
        print('Your guess is too low.')  # Print a string

    if guess > number:  # See that guess variable is higher than number variable
        print('Your guess is too high.')  # Print a string

    if guess == number:  # See that guess variable is equal to number variable
        break  # Break the while loop

if guess == number:  # See that guess variable is equal to number variable
    guessesTaken = str(guessesTaken)  # Change the guess variable to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Print string with
# myName and guessesTaken variables in it

if guess != number:  # See that guess variable is not equal to number variable
    number = str(number)  # Change the number variable to a string
    print('Nope. The number I was thinking of was ' + number)  # Print string with number variable
# at the end of the string
