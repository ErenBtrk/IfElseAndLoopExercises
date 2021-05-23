'''
36. Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle
'''

side1 = float(input("Please enter first side length : "))
side2 = float(input("Please enter second side length : "))
side3 = float(input("Please enter third side length : "))

if((side1 > side2+side3) or (side2 > side1+side3) or (side3 > side1+side2) or (side1 == 0) or
   (side2 == 0) or (side3 == 0) ):
    print("Its not a triangle.")
elif((side1 == side2) and (side2 == side3)):
    print("Equilateral triangle.")
elif((side1 == side2 and side3 != side1) or (side2 == side3 and side2 != side1) or 
      side1 == side3 and side1 != side2):
    print("Isosceles triangle.")
elif(side1 != side2 and side2 != side3 and side1 != side3):
    print("Scalene triangle.")
