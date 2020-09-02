a = 10
print(a, type(a))
print(isinstance(a, float))

b = [1, 2, "Reena"]
print(b)
print(b, type(b))

animals = ["cat", "dog"]
animals.append("pig")
print(animals)

vowels = ["a", "e", "i", "u"]

vowels.insert(3, "o")
print(vowels)

print("count",vowels.count("e"))


data = [1, 3, 4, 5, 7, 7, 8]
data.remove(7)
print(data)



my_tuple = ("h","h","e", "l", "o",1,6)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-2])
print(my_tuple[0:3])
print(my_tuple.count("h"))

name = [1, 2, 3, 4, 5, 67, 555, 8, 8]
print(name)
del name
# print(name.insert(6, 9999))  //    NameError: name 'name' is not defined

my_tuple1 = (1,2,3)
print(my_tuple1)
print(frozenset(my_tuple1))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset1 = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset2 = {"apple", "banana", "cherry"}
thisset2.add("kiwi")
print(thisset2)



