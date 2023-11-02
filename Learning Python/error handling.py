#try except is like a way to handle errors in python codes

#kunwari dito kapag pasaway si user at ginamit string imbis number

try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("That is not a number.")

#pwede rin magspecify ng error

try:
    eval("print(%d is a number)")
except SyntaxError as error:
    print("Caught a SyntaxError:", error)

#another situation is pag out of range ang inaaccess sa list

list = [1,2,3]

try:
    listnum = int(input("Enter a number from the list: "))
except IndexError as outofrange:
    print(outofrange)


