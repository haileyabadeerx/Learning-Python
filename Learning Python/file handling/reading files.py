import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the file path relative to the script's location
file_path = os.path.join(script_dir, "fontaine_charas.txt")

# Open the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)



#similar to file handling lesson in c
'''
fontaine = open("fontaine_charas.txt", "r")

print(fontaine.readable())

fontaine.close()
'''