'''
12. Write a Python program that accepts a sequence of lines (blank line to terminate)
 as input and prints the lines as output (all characters in lower case).
'''

lines = []

while True:
    userInput = input("Please enter : ").lower()
    if(not userInput):
        break
    else:
        lines.append(userInput)

print(lines)