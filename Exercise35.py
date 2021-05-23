'''
35. Write a Python program to check a string represent an integer or not.
Expected Output:

Input a string: Python                                                  
The string is not an integer. 
'''

str = input("Please enter a string : ")

if(str.isdigit()):
    print("The string is an integer.")
else:
    print("The string is not an integer.")

