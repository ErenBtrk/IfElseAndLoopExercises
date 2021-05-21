'''
26. Write a Python program to print the following patterns.
Expected Output:

  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 **** 

ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo 
'''

str = ""

for row in range(7):
    if(row == 0):
        str += " ****\n"
    elif(row == 1 or row == 2):
        str += "*\n"
    elif(row == 3):
        str += "***\n"
    elif(row == 4 or row == 5):
        str += "    *\n"
    else:
        str += "****\n"

print(str)

rowNum = int(input("Please enter size of row : "))
columnNum = int(input("Please enter size of column : "))

str2 = ""
cap = rowNum // 5
count = 0

for row in range(15):
    count += 1
    if(row < 3 or (row > 5 and row < 9) or row > 11):
        str2 += "o" *17 + '\n'
    elif(row < 6 and row > 2):
        str2 += "o" * 4 +'\n'
    else:
        str2 += (" " * 13)+ ("o" * 4) +'\n'

print(str2)