from characters import hsr_chara

char1 = hsr_chara("March 7th", "Preservation", 7777, False)

print(char1.name)

name = input("Character name: ")
path = input("Character's path: ")
age = input("Character's age: ")

char2 = hsr_chara(name, path, age, True)

print(char2.name)
print(char2.path)
print(char2.age)