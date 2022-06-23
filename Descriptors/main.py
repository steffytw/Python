"""
Python descriptors:

*   are created to manage the attributes of different classes which use the object as reference
*   is a mechanism behind properties, methods, static methods, class methods, and super()

Descriptor protocol :
    Python descriptor protocol is simply a way to specify what happens when an attribute is referenced on a model.

*   __get__(self, obj, type=None) accesses the attribute.

*   __set__(self, obj, value) is called in an attribute assignment operation.

*   __delete__(self, obj) controls a delete operation.

"""


class Descriptor(object):

    def __init__(self, name=''):
        self.name = name

    def __get__(self, obj, objtype):
        print(self,obj,objtype)
        print("Getting :", self.name)
        return self.name

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name.upper()
            print("Setting : ", self.name)
        else:
            raise TypeError("Name should be string")

    def __del__(self):
        print("Deleting : ", self.name)
        del self.name


class SetName(object):
    name = Descriptor()


set_name = SetName()
set_name.name = "tim"
print(set_name.name)
