name = input("Enter a String: ")
temp = name
rev = temp[::-1]
if temp == rev:
    print(rev, "is pallaindrom ")
else:
    print(rev, "is not a pallaindrom ")