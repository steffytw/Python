from calculatorFunction import add, mul, sub, div

a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
inputData = input("select your choice(add,sub,div,mul) :")

if inputData == "add":
    print(add(a, b))
elif inputData == "sub":
    sub(a, b)
elif inputData == "div":
    div(a, b)
elif inputData == "mul":
    mul(a, b)
