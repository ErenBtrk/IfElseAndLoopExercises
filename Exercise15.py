'''
15. Write a Python program to check the validity of password input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''

import re

while True:
    try:
        password = input("Please enter a password : ")
        if(not re.search("[a-z]",password)):
            raise Exception("Password should include atleast 1 lower case letter.")
        elif(not re.search("[A-Z]",password)):
            raise Exception("Password should include atleast 1 upper case letter.")
        elif(not re.search("[$#@]",password)):
            raise Exception("Password should include atleast one of $,#,@ these characters.")
        elif(len(password)<6 or len(password)>16):
            raise Exception("Password should 6-16 characters.")
    except Exception as excObject:
        print(excObject)
    else:
        break

login = input("Please enter your password : ")
if(login == password):
    print("Valid password.")
else:
    print("Invalid password.")


