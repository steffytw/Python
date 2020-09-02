# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("Hello my age is " + self.age)

class Person:
    def __init__(self,age):
        self.age = age

    def myfunc(self):
        print("Hello my age is " + self.age)


p1 = Person("36")
p1.myfunc()

p1.age = "40"
p1.myfunc()

print(p1.age)


