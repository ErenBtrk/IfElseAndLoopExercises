'''
34. Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20.
'''

def addition(num1,num2):
    sum = num1 + num2
    if(sum > 15 and sum < 20):
        return 20
    else:
        return sum

number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))

print(addition(number1,number2))