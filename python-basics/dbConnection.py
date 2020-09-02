import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PYTHON_DATA"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE PYTHON_DATA")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
# mycursor.execute("CREATE TABLE STUDENT_DATA(NAME VARCHAR(50), AGE VARCHAR(3),STUDENT_ID VARCHAR(10) PRIMARY KEY)")

# mycursor.execute("INSERT INTO STUDENT_DATA(NAME, AGE, STUDENT_ID)VALUES('REMYArrere',10,1105)")
# mycursor.execute("INSERT INTO STUDENT_DATA(NAME, AGE, STUDENT_ID)VALUES('AYRA',12,1012)")
# mycursor.execute("INSERT INTO STUDENT_DATA(NAME, AGE, STUDENT_ID)VALUES('YASH',16,1103)")
# mycursor.execute("INSERT INTO STUDENT_DATA(NAME, AGE, STUDENT_ID)VALUES('YAMINI',20,1104)")
# sql = "INSERT INTO STUDENT_DATA(NAME,AGE,STUDENT_ID) VALUES(%s,%s,%s)"
# val = ('AARIYA', '21', '2105')
# val = [('RIYA','21','105'),('MIYA','25','106'),('MIYAYA','25','107')]
# mycursor.executemany(sql, val)
# mycursor.execute(sql, val)

mydb.commit()
mycursor.execute("SELECT * FROM STUDENT_DATA")
cur = mycursor.fetchall()
for i in cur:
    print(i)
