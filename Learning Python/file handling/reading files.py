#similar to file handling lesson in c

fontaine = open(r"D:\github\Learning Python\Learning Python\file handling\fontaine_charas.txt", "r")
#may r sa unahan para maread as raw string since path lang nareread ko hindi yung file lang
print(fontaine.read())

fontaine.close()
