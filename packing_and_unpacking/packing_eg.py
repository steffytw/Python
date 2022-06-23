def Sum(*args):
    return sum(args)


# Driver code
print(Sum(1, 2, 3, 4, 5))
print(Sum(10, 20))



def fun(*args):
    print(*args)


# Driver Code
my_list = [1, 2, 3, 4]


fun(my_list)