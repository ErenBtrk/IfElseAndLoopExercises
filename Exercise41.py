'''
41. Write a Python program to get next day of a given date.
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24
'''



monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]

year = int(input("Please enter year : "))
month = int(input("Please enter month : "))
day = int(input("Please enter day : "))

day += 1

if(day > monthDays[month-1]):
    day = 1
    month += 1
if(month > 12):
    month = 1
    year += 1

print(str(year)+'-'+str(month)+'-'+str(day))