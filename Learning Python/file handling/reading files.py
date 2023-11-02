'''
import os

# Get the directory of your Python script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the file name you want to check
file_name = "fontaine_charas.txt"

# Construct the full path to the file
file_path = os.path.join(script_directory, file_name)

# Check if the file exists
if os.path.isfile(file_path):
    print(f"The file '{file_name}' is in the same directory as your Python script.")
else:
    print(f"The file '{file_name}' is not in the same directory as your Python script.")

import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the file path relative to the script's location
file_path = os.path.join(script_dir, "fontaine_charas.txt")

# Open the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
'''


#similar to file handling lesson in c

fontaine = open("fontaine_charas.txt", "r")

print(fontaine.read())

fontaine.close()
