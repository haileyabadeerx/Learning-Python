from characters import gi_chara

name = input("Character name: ")
element = input("Character's element: ")
weapon = input("Character's weapon: ")
age = input("Character's age: ")

char = gi_chara(name, element, weapon, age)

print(char.name)
print(char.element)
print(char.weapon)
print(char.age)
print(char.age_range())