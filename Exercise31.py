'''
31. Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. 
After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73

'''

dogAge = int(input("Please enter dog's age : "))
humanAge = 0

if(dogAge <= 2):
    humanAge = dogAge * 10.5
else:
    humanAge = (2 * 10.5) + (dogAge - 2)*4

print(f"The dog's age in dog's years is {humanAge:.0f}")