class emp:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def display(self):
        print("name:{},{} years old".format(self.__name,self.__age))


e1 = emp("ram",34)
e1.display()
e1.__age = 55
print(e1.__age)
e1.display()
e1.display()
e1._emp__age=70
e1.display()