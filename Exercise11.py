'''
11. Write a Python program which takes two digits m (row) and n (column) as input and generates
a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
'''

rowNum = int(input("Please enter row : "))
columnNum = int(input("Please enter column : "))

matrix = [[0 for col in range(columnNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(columnNum):
        matrix[row][col] = row*col

print(matrix)