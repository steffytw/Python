class student:
    course = "Python"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self, address):
        print("I am {},{} years old".format(self.name, self.age))
        print("I am from ", address)


student1 = student("John", 25)
student1.display("TVM")
print(student1.course)
# student2 = student("Reeba", 33)
# student2.course = "Angular"
# student2.display("TVM")
# print(student2.course)
# student1.name = "John R"
# student1.display("TVM")
