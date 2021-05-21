'''
21. Write a Python program to print alphabet pattern 'L'.
Expected Output:

 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****
'''
str = ""

for row in range(7):
    if(row == 6):
        str += "*****\n"
    else:
        str += "*\n"

print(str)