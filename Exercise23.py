'''
23. Write a Python program to print alphabet pattern 'O'.
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
'''

str = ""

for row in range(7):
    if(row == 0 or row == 6):
        str += " *** \n"
    else:
        str += "*   *\n"

print(str)
