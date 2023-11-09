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

print(phrase[2])#to print a specify chara in a str (parang gumamit ng array)

print(phrase.index("n")) #ibibigay ng program anong index nung char na nandito
                        #pag naglagay ng sumthing na wala dito mag eerror
                        #pag ata may nauulit na char ung una lang madedetect?

print(phrase.replace("Genshin", "Honkai")) #para mareplace yung nakalagay sa string
                    