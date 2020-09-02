import mysql.connector

db1 = mysql.connector.connect(
    host="192.168.1.250",
    user="scopeinternship",
    password="scopeinternship",
    database="scopeinternship"
)
cursor_data = db1.cursor()
cursor_data.execute("SELECT * FROM STUDENT_DETAILS_STEFFY")
cur = cursor_data.fetchall()
for i in  cur:
    print(i)
