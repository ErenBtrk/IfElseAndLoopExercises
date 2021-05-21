'''
17. Write a Python program to print alphabet pattern 'A'.
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
'''

str = ""

for row in range(7):
    if(row == 0):
        str += " ***\n"
    elif(row == 3):
        str += "*****\n"
    else:
        str += "*   *\n"

print(str)