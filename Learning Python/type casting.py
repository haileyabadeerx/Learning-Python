#trying to make a simple addition calcu here to show how type casting works

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = num1 + num2 #di pa naka type casting so inadd sya as strings kaya wrong value
print(result)

result = float(num1) + float(num2)
print(result)

result = int(num1) + int(num2) #ito magiging tama na kasi naconvert na to int pero pag naglagay decimal mag eerror
print(result)