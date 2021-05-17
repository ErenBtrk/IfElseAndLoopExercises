'''
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''

temperature = input("Please enter the temperature : ")
type = temperature[-1].lower()
degree = float(temperature[:-1])
print(type)
print(degree)

if(type == 'c'):
    print(f"{degree} celsius is {1.8*degree+32} fahrenheit")
elif(type == 'f'):
    print(f"{degree} fahrenheit is {(degree-32)*(5/9)} celcius")
else:
    print("Invalid temperature type.")




