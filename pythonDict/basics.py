dict1 = {1: "one", 2: "three"}
dict2 = {2: "two"}
dict3 = {3: "four"}
print(dict1)
print(dict1.items())  # dictionary items
print(dict1.keys())  # dictionary keys
print(dict1.values())  # dictionary values
dict1.update(dict2)  # update dict1 with dict2
print(dict1)
dict1.update(dict3)  # update dict1 with dict3
print(dict1)

a = "Hello World!"
print(a.split(" "))