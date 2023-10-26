print("\n\nThis is how to use\n \"string")

#or we can instead use variables to store strings

phrase = "Genshin Impact"

print(phrase + " is such a cool game") #<--this is called concatenation 

print(phrase.lower()) #function to print all strings lowercase
print(phrase.upper()) #function to print all strings uppercase

print(phrase.islower()) #pwede rin islower to check if ganon sila
print(phrase.isupper()) #pwede rin islower to check if ganon sila

#to combine the two funcs sa isang print para maconvert at maging true
print(phrase.upper().isupper()) 
print(phrase.lower().islower())

print(len(phrase)) #function to check how many chara in a string

print(phrase[0])#to print a specify chara in a str (parang gumamit ng array)