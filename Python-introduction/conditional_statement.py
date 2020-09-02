# a = input("Enter first number :")
# b = input("Enter second number :")
# if a > b:
#     print("{} is greater than {}".format(a, b))
# else:
#     print("{} is greater than {}".format(b, a))

a = input("Enter first number :")
b = input("Enter second number :")
if b > a:
  print("{} is greater than {}".format(b, a))
elif a == b:
  print("Both are equal:{}=={}".format(a, b))
else:
    print("{} is greater than {}".format(a, b))
