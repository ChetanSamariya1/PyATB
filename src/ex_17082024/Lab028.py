# Escape Sequence
print("Hello World")
print("Hello \nWorld") # \n -> To create new line
print("Hello \tWorld") # \t -> To create new tab line
print("Hello \bWorld") # \t -> Back space

#dir = 'C:\Chetan\n.text'
#dir = "C:\Chetan\n.text"
# Where r concept will be used?
# r means row string
# Automation API, Web Automation, file_path
dir1 = r"C:\Chetan\n.text"  # To avoid \n conversation, "r" can be used
dir2 = r'C:\Chetan\n.text'  # r can work with single and double quote both

print(dir1)
print(dir2)

""" Single and double quotes both can be used in Python
 single quote can be used between double quote
 but double quote can not be used between single quote
 For Single Quote, we need to use escape sequence
"""
name = 'Chetan'
name2 = "Chetan"
name3 = "Chetan'S"
name4 = 'Chetan\"S'
print(name, name2, name3, name4)
