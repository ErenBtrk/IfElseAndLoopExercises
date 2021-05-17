'''
5. Write a Python program that accepts a word from the user and reverse it.
'''

word = input("Please enter a word : ")
word = list(word)
word.reverse()
print(word)

string = ""

for i in word:
    string += i

print(string)