fontaine = open(r"D:\github\Learning Python\Learning Python\file handling\fontaine_charas.txt", "a")

add_char = input("Enter a fontaine character: ")

fontaine.write(add_char)

fontaine.close()
'''
newfile = open(r"try.html", "w")

newfile.write("<p> Hello World </p>" )

print(newfile.read())

newfile.close()
'''

newfile = open(r"D:\github\Learning Python\Learning Python\file handling\try.html", "r")
print(newfile.read())

newfile.close()