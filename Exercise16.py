'''
16. Write a Python program to find numbers between 100 and 400 (both included)
 where each digit of a number is an even number. The numbers obtained should be
printed in a comma-separated sequence.
'''

def isEven(number):
    digit = 0
    while(number > 0):
        digit = number % 10
        number = number // 10
        if(digit % 2 != 0):
            return False
    return True

numbers = []

for i in range(100,401):
    if(isEven(i)):
        numbers.append(str(i))

print(",".join(numbers))

