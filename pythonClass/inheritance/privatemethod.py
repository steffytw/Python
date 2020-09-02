class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

        # private member function

    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

        # public member function

    def accessPrivateFunction(self):
        # accesing private member function
        self.__displayDetails()



obj = Geek("R2J", 1706256, "Information Technology")
obj.accessPrivateFunction()