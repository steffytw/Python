class Person:
    def __init__(xyz, name, age):
        xyz.name = name
        xyz.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
