a = int(input("Please Enter any Number: "))
temp = a
s = 0
while temp > 0:
    r = temp % 10
    s = s + r ** 3
    temp = temp // 10

if a == s:
    print(a, "amstrong")
else:
    print(a, " not amstrong")
