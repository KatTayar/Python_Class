
#Exercise 4:

#Write a program named TestRandom that generates a random integer and asks the user to guess what the generated number is. 
#If the user’s guess is higher than the random number, the program should display, “Too high, try again”. If the user’s guess is lower than the random number, 
#the program should display, “Too low, try again”. The program should use a loop that repeats until the user enters correctly guesses the random number 
#at which point the program will display, “Bravo, you got it!”.
#NB: You can generate a random number in python in two steps:
#First import the random number generator using: import random
#Second, get a random number using: number = random.randint(min, max)
#For example, random.randint(0, 1) will generate either 0 or 1, and random.randint(1, 100) will generate an integer    greater than 0 but less than 101.

#Exercise 5:

 #Modify your TestRandom program from exercise 3 so that the program keeps a count of the number of attempts the user makes to correctly guess the random number. 
#Update the winning message to be: “Bravo! Bravo! You correctly guessed my random number in” xx “attempts”, where xx represents the total attempts by the user.

import random

min_number = 1
max_number = 100
random_number = random.randint(min_number, max_number)

guess = None
attempt = 0
while guess != random_number:
    guess = int(input("Guess the number between {} and {}: ".format(min_number, max_number)))
    attempt += 1
    if guess > random_number:
        print("Too high, try again.")
    elif guess < random_number:
        print("Too low, try again.")
    else:
        print("Bravo! Bravo! You correctly guessed my random number in", attempt, "attempts")
