'''
25. Write a Python program to print alphabet pattern 'R'.
Expected Output:

 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 * *                                                                    
 *  *                                                                   
 *   *
'''

str = ""

for row in range(7):
    if(row == 0 or row == 3):
        str += "****\n"
    elif(row == 1 or row == 2):
        str += "*   *\n"
    elif(row == 4):
        str += "* *\n"
    elif(row == 5):
        str += "*  *\n"
    else:
        str += "*   *\n"

print(str)