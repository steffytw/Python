import hashlib

password = 'password123'
salt= '123'+password
print(salt)
obj = hashlib.md5(salt.encode())
passwordEncryption = obj.hexdigest()
print(obj)
print(passwordEncryption)

# password1 = b'password123'
# salt1= b'@@@'+password1
# print(salt1)
# obj1 = hashlib.sha1(salt1)
# passwordEncryption1 = obj1.hexdigest()
# print(obj1)
# print(passwordEncryption1)