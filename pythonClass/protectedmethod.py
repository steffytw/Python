class Student:
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

        # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

    # derived class
class Geek(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


obj = Geek("R2J", 1706256, "Information Technology")
obj.displayDetails()