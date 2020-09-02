import calculatorFunction

a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
inputData = input("select your choice(add,sub,div,mul) :")


if inputData == "add":
    print(calculatorFunction.add(a, b))
elif inputData == "mul":
    calculatorFunction.mul(a, b)
elif inputData == "sub":
    calculatorFunction.sub(a, b)
elif inputData == "div":
    calculatorFunction.div(a, b)
