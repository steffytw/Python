import re

txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

txt1 = "That will be 588889 dollars"

# Find all digit characters:

x1 = re.findall("\d", txt1)
print(x1)

txt2 = "hello world"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x2 = re.findall("he..o", txt2)
print(x2)

txt3 = "hello world"

# Check if the string starts with 'hello':

x3 = re.findall("^h", txt3)
if x3:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

txt4 = "The rain in Spain falls  all mainly in the plain!"

# Check if the string contains "a" followed by exactly two "l" characters:

x4 = re.findall("al{2}", txt4)

print(x4)

if x4:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt5 = "The rain in Spain falls stays mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x5 = re.findall("falls|stays", txt5)

print(x5)

if x5:
    print("Yes, there is at least one match!")
else:
    print("No match")


txt8 = "The rain in Spain  falls mainly in the plain aix!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x8 = re.findall("Spaix*", txt8)

print(x8)

if (x8):
  print("Yes, there is at least one match!")
else:
  print("No match")

txt9 = "The rain in Spain falls mainly in the plain aix !"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x9 = re.findall("aix+", txt9)

print(x9)

if (x9):
  print("Yes, there is at least one match!")
else:
  print("No match")
