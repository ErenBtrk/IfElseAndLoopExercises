'''
14. Write a Python program that accepts a string and calculate the number
 of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
'''

string = input("Please enter a string : ")
digitNum = 0
letterNum = 0

for item in string:
    if(item.isalpha()):
        letterNum += 1
    if(item.isdigit()):
        digitNum += 1

print(string)
print(f"Number of digits = {digitNum}\nNumber of Letters = {letterNum}")