'''
6. Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenCount = 0
oddCount = 0

for item in numbers:
    if(item % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1

print(f"Even number count = {evenCount}")
print(f"Odd number count = {oddCount}")
