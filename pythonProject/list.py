a = 10
print(a, type(a))
print(isinstance(a, int))

b = [1, 2, "Reena"]
print(b)
print(b, type(b))

animals = ["cat", "dog"]
animals.append("pig")
print(animals)

vowels = ["a", "e", "i", "u"]

vowels.insert(3, "o")
print(vowels)

print(vowels.count("e"))


data = [1, 3, 4, 5, 7, 7, 8]
data.remove(7)
print(data)



my_tuple = ("h", "e", "l", "o")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

name = [1, 2, 3, 4, 5, 67, 555, 8, 8]
print(name)
del name
# print(name.insert(6, 9999))  //    NameError: name 'name' is not defined
