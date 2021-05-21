'''
18. Write a Python program to print alphabet pattern 'D'. 
Expected Output:

****                                                                   
*   *                                                                  
*   *                                                                  
*   *                                                                  
*   *                                                                  
*   *                                                                  
**** 
'''

str = ""

for i in range(7):
    if(i == 0 or i == 6):
        str += "****\n"
    else:
        str += "*   *\n"

print(str)