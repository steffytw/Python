a=[1,3,45,5,2]
t=0
for i in a:
    if t<i:
        t = i
    else:
        continue
print(t)