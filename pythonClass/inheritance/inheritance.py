class Bird:

    def __init__(self):
        print("bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("bird is swimming")


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def Run(self):
        print("Penguin can  Run faster ")


peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.Run()
