file = open("student.txt","r")
"""
print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
file.close()"""

"""
txt = file.readlines()
print(txt)

file.close()"""
"""
txt = file.readlines()[1]
print(txt)

file.close()

"""


for line in file:
   print(line)
file.close()

