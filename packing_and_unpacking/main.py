# packing and unpacking of arguments


def add_numbers1(x, y):
    result = x + y
    print(result)


add_numbers1(1, 2)


def add_numbers2(*args):
    result = sum(args)
    print(f'REsult{result}')


add_numbers2(1, 2, 8, 9)


def add_numbers3(*args):
    print(args)
    result = sum(args)
    print(result)


my_list = [1, 2, 3, 4, 5]

add_numbers3(*my_list)


def contacts1(alice, blob):
    print(alice)
    print(blob)


contacts1(alice=62653656, blob=93988783)


def contacts2(**kwargs):
    print(kwargs)


contacts2(alice=62653656, blob=93988783, elice=45674547)


#

def contacts3(**kwargs):
    print(kwargs)


my_dict = {'alice': 3949389, 'blob': 85768758, 'elice': 7384787}

contacts3(**my_dict)
