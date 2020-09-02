import re

txt = "The rain 123 ***+++ in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[0-9][0-9][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")