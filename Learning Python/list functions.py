ages = [9, 14, 15, 16, 20, 21]
names = ["Hail", "Kendra", "McDuffie", "Maeve", "Hailey", "HailStorm"]

print("Normal printing of lists:")
print(names)
print(ages)

#to search for an index
print(names.index("Maeve"))

#to append another list to a list
names.extend(ages)
print(names)

#to append something on just 1 list
ages.append(13)
print(ages)

#to insert on specific element
ages.insert(0, 7)
print(ages) #once na may ininsert, lahat mapupush

#to remove an element
names.remove("McDuffie")
print(names)

#remove the last element of the list
names.pop()
print(names)

#remove every element/ clear the list
ages.clear()
names.clear()
print(names)
print(ages)