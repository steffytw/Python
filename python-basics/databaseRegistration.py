import mysql.connector
import hashlib

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arathil123@",
    database="STUDENT_INFO"
)
mycursor = db.cursor()


def hashing(password):
    password = password+"123"
    obj = hashlib.md5(password.encode())
    passwordEncryption = obj.hexdigest()
    return passwordEncryption


userChoice = input("ENTER YOUR CHOICE(register,login):")
if userChoice == "register":

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

elif userChoice == "login":
    login_username = input("ENTER YOUR USERNAME:")
    login_password = input("ENTER YOUR PASSWORD:")
    hashed_password = hashing(login_password)
    data = mycursor.execute(
        "SELECT USERNAME,PASSWORD FROM STUDENT_DATA WHERE USERNAME ='{}' AND PASSWORD ='{}'".format(login_username,hashed_password))
    result = mycursor.fetchall()
    if len(result) == 1:
        print("Hello " + login_username)
    else:
            print(" INVALID USERNAME OR PASSWORD ")

