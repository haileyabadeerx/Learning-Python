def addition(a, b):
    result = int(a) + int(b)
    return result

def subtraction(a, b):
    result = int(a) - int(b)
    return result

def multiplication(a, b):
    result = int(a) * int(b)
    return result

def division(a, b):
    result = int(a) / int(b)
    return result

print("This program can calculate basic operations.")

print("Please enter 2 numbers: ")
num1 = input()
num2 = input()
is_invalid = False

print("Please input the operation you wish to perform: ")
op = input()

if op == "+":
    answer = addition(num1, num2)
elif op == "-":
    answer = subtraction(num1, num2)
elif op == "*":
    answer = multiplication(num1, num2)
elif op == "/":
    answer = division(num1, num2)
else:
    print("Invalid input.")
    is_invalid = True

if is_invalid:
    print("Try again.")
else:
    print("The answer is " + str(answer))