n = int((input("enter the number :")))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


for num in range(0, n):
    print(fib(num))
