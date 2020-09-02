import mysql.connector
import hashlib

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arathil123@",
    database="STUDENT_INFO"
)
mycursor = db.cursor()


# mycursor.execute("CREATE DATABASE STUDENT_INFO")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

def hashing(password):
    obj = hashlib.md5(password.encode())
    passwordEncryption = obj.hexdigest()
    return passwordEncryption


# mycursor.execute("CREATE TABLE STUDENT_DATA(ID INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(10),USERNAME VARCHAR(10),PASSWORD INT) ")
mycursor.execute("ALTER TABLE  STUDENT_DATA MODIFY PASSWORD VARCHAR(100)")
a = input("ENTER YOUR NAME:")
b = input("ENTER YOUR USERNAME:")
c = input("ENTER YOUR PASSWORD:")
d = input("CONFIRM PASSWORD:")

if c == d:
    encryptedData = hashing(c)
    mycursor.execute(
        "INSERT INTO STUDENT_DATA(NAME,USERNAME,PASSWORD) VALUES('" + a + "','" + b + "','" + encryptedData + "')")
    db.commit()
else:
    print("INVALID PASSWORD OR CONFIRM PASSWORD")


