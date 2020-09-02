class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name of the student :{}    Age:{}   Gender:{}".format(self.name, self.age, self.gender))


class marks:
    def __init__(self, studentClass, eng, maths, phy, chem):
        self.studentClass = studentClass
        self.eng = eng
        self.maths = maths
        self.phy = phy
        self.chem = chem

    def display(self):
        print("student in : ", self.studentClass)
        print("Total marks : ", self.eng + self.maths + self.phy + self.chem)


class student(person, marks):
    def __init__(self, name, age, gender, studentClass, eng, maths, phy, chem):
        person.__init__(self, name, age, gender)
        marks.__init__(self, studentClass, eng, maths, phy, chem)

    def result(self):
        person.display(self)
        marks.display(self)


student1 = student("rekha", 25, "female", "2A", 78, 34, 88, 90)
student1.result()
