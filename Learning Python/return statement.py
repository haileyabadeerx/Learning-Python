def rectangle_area(L, W):
    area = int(L) * int(W)
    return area

length = input("Enter length: ")
width = input("Enter width: ")

area = rectangle_area(length, width)

print(area)