#trying to make a simple addition calcu here to show how type casting works

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = num1 + num2 #di pa naka type casting so inadd sya as strings kaya wrong value
print(result)

result = int(num1) + int(num2)
print(result)