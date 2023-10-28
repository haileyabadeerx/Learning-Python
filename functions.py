def greetings(name, days):
    print("Welcome to functions in Python")
    print("Nice meeting you " + name + ". \n So you are learning Python for " + str(days) + " days.")

#to call a function with passing parameters
print("This is how function works in Python")
nam = input("Your name? ")
das = input("How long are you learning python?")
greetings(nam, das)
print("Kewl, isn't it?")