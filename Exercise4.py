'''
4. Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

n= 10


for j in range(1,n+1):
    print('*'*j)
i = n-1
for j in range(n,0,-1):
    print('*'*i)
    i-=1