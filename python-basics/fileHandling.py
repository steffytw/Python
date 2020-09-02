# file handling
# from pip._internal.utils import encoding

fp = open('sample.txt', 'r', encoding='utf-8')
# demo = fp.read(10)
# print(demo)
# print(fp.readlines())
# print(fp.readline())
# for line in fp:
#     print(line)
# f1 = open('demo.txt', 'a', encoding='utf-8')
# f1.write('#############')
f1 = open('demo.txt', 'r+', encoding='utf-8')
print(f1.read())

f1.close()
fp.close()
