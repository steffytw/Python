class person:
    def __init__(self):
        self.name = input("name: ")
        self.age = input("age: ")
        self.gender = input("gender: ")

    def display(self):
        print("Name of the student :{}    Age:{}   Gender:{}".format(self.name, self.age, self.gender))


class marks:
    def __init__(self):
        self.studentClass = input("studentClass :")
        self.eng = int(input("eng :"))
        self.maths = int(input("maths :"))
        self.phy = int(input("phy :"))
        self.chem = int(input("chem :"))

    def display(self):
        print("student in : ", self.studentClass)
        print("Total marks : ", self.eng + self.maths + self.phy + self.chem)


class student(person, marks):
    def __init__(self):
        person.__init__(self)
        marks.__init__(self)

    def result(self):
        person.display(self)
        marks.display(self)


student1 = student()
student1.result()
