try:
    num = int(input("Enter a number: "))
    if num <= 5:
        raise Exception("\nnumber should be greater than 5")
except Exception as e:
    print("error", e)

else:
    print(num, "is greater the 5")
