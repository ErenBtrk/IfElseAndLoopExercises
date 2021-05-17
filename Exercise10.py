'''
10. Write a Python program which iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for the multiples
of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
'''



for i in range(1,51):
    flag1 = False
    flag2 = False
    if(i % 3 == 0):
        flag1 = True
    if(i % 5 == 0):
        flag2 = True
    if(flag1 and not flag2):
        print("Fizz")
    elif(not flag1 and flag2):
        print("Buzz")
    elif(flag1 and flag2):
        print("FizzBuzz")
    else:
        print(i)        


