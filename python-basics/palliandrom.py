a = int(input("Enter any Number: "))
temp=a
s = 0
while a > 0:
    r = a % 10
    s = (s * 10) + r
    a = a // 10
print(s)

if s == temp:
    print(s, "is pallaindrom number")
else:
    print(s, "is  not a pallaindrom number")
