'''
42. Write a Python program to calculate the sum and average of n integer numbers 
(input from the user).Input 0 to finish.
'''

sum = 0
count = 0
number = -1

while number != 0:
    number = int(input("Please enter a number : "))
    sum += number
    count += 1

print(f"Sum = {sum} and Average = {float(sum/(count-1))}")