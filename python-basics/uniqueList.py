l1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 1]


def unique():
    l2 = list()
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)


unique()
