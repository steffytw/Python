import hashlib

password = b'password123'
obj = hashlib.sha1(password)
passwordEncryption = obj.hexdigest()
print(obj)
print(passwordEncryption)
