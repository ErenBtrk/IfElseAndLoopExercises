'''
9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''

a = 1
b = 1
c = a+b

while a < 50:
    print(a)
    a = b
    b = c
    c = a+b

#########################################################################################################

x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y