n = int(input("Enter the no of rows: "))


def alphaPyramid(n):
    b = 65
    for i in range(0, n):
        b = 65
        for j in range(0, i + 1):
            a = chr(b)
            print(a, end=" ")
            b = b + 1
        print("\r")


alphaPyramid(n)
