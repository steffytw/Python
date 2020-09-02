rows = int(input(" Enter Number of Rows: "))
num = 65
for i in range(0, rows):
    for j in range(0, i + 1):
        a = chr(num)
        print(a, end=" ")
        num = num + 1
    print("\r")
