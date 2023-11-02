#similar to file handling lesson in c

fontaine = open(r"D:\github\Learning Python\Learning Python\file handling\fontaine_charas.txt", "r")
#may r sa unahan para maread as raw string since path lang nareread ko hindi yung file lang
print(fontaine.readable()) #<-- check if the file is readable
print(fontaine.readline()) #<-- just reads an indvidual line (by default, yung una lang mareread nya)
print(fontaine.readline())
print(fontaine.readline())

print(fontaine.read()) #<-- read everything in the file

fontaine = open(r"D:\github\Learning Python\Learning Python\file handling\fontaine_charas.txt", "r")
print(fontaine.readlines()[3])



fontaine.close()
