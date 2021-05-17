'''
3. Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''

import random

randomNumber = random.randint(1,10)

while True:
    while True:
        try:
            number = int(input("Please enter a number : "))
        except Exception as excObject:
            print(excObject)
        else:
            break
    if(number == randomNumber):
        print("Well guessed!!!")
        break
    elif(number > randomNumber):
        print("Too high.")
    else:
        print("Too low.")
    

