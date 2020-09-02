import re

txt = "The rain in 5 Spain"

# Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if (x):
    print("Yes, there is a match!")
else:
    print("No match")
#Check if "ain" is present at the beginning of a WORD:

x1 = re.findall(r"\bain", txt)

print(x1)

if x1:
    print("Yes, there is at least one match!")
else:
    print("No match")

x2 = re.findall(r"\Bain", txt)

print(x2)

if (x2):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


x = re.findall("\s", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\W", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")