#try except is like a way to handle errors in python codes

#kunwari dito kapag pasaway si user at ginamit string imbis number

try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("That is not a number.")

#pwede rin magspecify ng error

try:
    print(%d is a number", num)
except SyntaxError as error: #errors can have names
    print(error)
