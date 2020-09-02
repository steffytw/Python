from curses.ascii import isupper, islower

a = "This is a paragraph"
temp = a


def cal():
    count = 0
    count1 = 0
    for i in a:
        if i.isupper() >= 1:
            count = count + 1
        elif i.islower() >= 1:
            count1 = count1 + 1
    print("The number of uppercase is", count)
    print("The number of lowercase is", count1)


cal()
