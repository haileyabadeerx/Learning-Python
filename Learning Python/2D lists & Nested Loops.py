twodimension_list = [
    [1, 2, 3], #row 0
    [4, 5, 6], #row 1
    [7, 8, 9], #row 2
    [0] #row 3
] 

row = int(input("What row you want to see?"))
column = int(input("What column you want to see?"))

print(twodimension_list[row][column]
      
#can use nested for loop for printing 2d list
for row in twodimension_list:
    for column in row:
        print(column)