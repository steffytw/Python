class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("I am {},{} years old".format(self.name, self.age))


student1 = student("John", 25)
student1.display()

# student2 = student("Reeba", 33)
# student2.display()

student1.name = "John R"
student1.display()
student1.age = "22"
student1.display()
# student3 = student("Reena")
# student3.display()
