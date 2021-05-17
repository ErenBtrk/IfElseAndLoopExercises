'''
13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
 as its input and print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
'''

def binaryToDecimal(num):
    total = 0
    num = list(str(num))
    j=0
    for i in range(len(num)-1,-1,-1):
        total += int(num[i])*(2**j)
        j += 1
    return total

        

userInput = input("Please enter binary numbers separated by comma : ").split(",")

for item in userInput:
    newItem = binaryToDecimal(item)
    if(newItem % 5 == 0):
        print(item)

####################################################################################################

items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2) #convert decimal to binary
    if not x%5:
        items.append(p)
print(','.join(items))


print(int("1000",2)) #convert decimal to binary