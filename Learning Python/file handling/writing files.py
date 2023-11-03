fontaine = open(r"D:\github\Learning Python\Learning Python\file handling\fontaine_charas.txt", "a")

add_char = input("Enter a fontaine character: ")

fontaine.write(add_char)

fontaine.close()