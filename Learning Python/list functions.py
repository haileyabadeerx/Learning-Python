ages = [9, 14, 15, 16, 20, 21]
names = ["Hail", "Kendra", "McDuffie", "Maeve", "Hailey", "HailStorm"]

print("Normal printing of lists:")
print(names)
print(ages)

#to append another list to a list
names.extend(ages)
print(names)

#to append something on just 1 list
ages.append(13)
print(ages)