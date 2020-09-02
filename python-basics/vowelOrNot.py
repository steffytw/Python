inputData = input("Enter a string :")
temp = inputData


def vowelsOrNot():
    l1 = list()
    l2 = list()
    for i in temp:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            # print(i, "is a vowel")
            l1.append(i)

        else:
            # print(i, "is a consonant")
            l2.append(i)

    print(l1, "are vowels")
    print(l2, "are consonants")


vowelsOrNot()
