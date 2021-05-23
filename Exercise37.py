'''
37. Write a Python program that reads two integers representing a month
 and day and prints the season for that month and day. 
Expected Output:

Input the month (e.g. January, February etc.): july                     
Input the day: 31                                                       
Season is autumn  
'''

months = ["january","february","march","april","may","june",
          "july","august","september","october","november","december"]

monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    try:
        month = input("Please enter month : ")
        day = int(input("Please enter day : "))
        if(not month in months):
            raise Exception("Wrong month name.")
        if(day <0 or day > monthDays[months.index(month)]):
            raise Exception("Wrong day.")
    except Exception as excObject:
        print(excObject)
    else:
        break

monthIndex = months.index(month)
print(monthIndex)

if( (monthIndex >= 0 and monthIndex < 2 ) or monthIndex == 11):
    print("Season is winter.")
elif(monthIndex >= 2 and monthIndex <5):
    print("Season is spring.")
elif(monthIndex >= 5 and monthIndex <8):
    print("Season is summer.")
else:
    print("Season is autumn.")
    

        
