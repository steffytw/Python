import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x1 = re.search("^The .* Spain$", txt)
x8 = re.search("\s", txt)
# print(x1)
print("The first white-space character is located in position:", x8.start())


if x1:
    print("match")
else:
    print("not match")

x2 = re.split("\s", txt)
print(x2)

x3 = re.sub("\s", ",", txt)
print(x3)
