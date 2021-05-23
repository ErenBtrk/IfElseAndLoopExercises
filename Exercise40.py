'''
40. Write a Python program to find the median of three values.
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0
'''

list = []

i = 0

while i<3:
    number = int(input("Please enter a number : "))
    list.append(number)
    i += 1

list.sort()

print(f"The median is {list[1]}")