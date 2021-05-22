'''
30. Write a Python program to print alphabet pattern 'Z'.
Expected Output:

*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******

'''

str = ""
spaceCount = 5

for row in range(7):
    if(row == 0 or row == 6):
        str += "*******\n"
    else:
        str += (' ' * spaceCount) + '*\n'
        spaceCount -= 1

print(str) 