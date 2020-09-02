a = ['anitha', 'haritha', 'ann', 'u']
count = 0
for i in a:
    if len(i) > 2 and i[0] == i[-1]:
        count = count + 1
print(count)
