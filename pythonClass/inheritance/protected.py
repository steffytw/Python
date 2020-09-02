class emp:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display(self):
        print("name:{},{} years old".format(self._name, self._age))


e1 = emp("ram", 34)
e1.display()
e1._age = 55
e1.display()
