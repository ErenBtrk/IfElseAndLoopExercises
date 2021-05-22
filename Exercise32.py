'''
32. Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.

'''

vowels = "aeiou"

letter = input("Please enter a letter : ").lower()

if(letter in vowels):
    print(f"The letter({letter}) you have entered is a vowel.")
else:
    print(f"The letter({letter}) you have entered is a consonant.")