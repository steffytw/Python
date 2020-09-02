import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arathil123@",
    database="CATEGORIES"
)

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE CATEGORIES")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE FLIPCART_CATEGORIES(CATEGORY_ID INT(5) PRIMARY KEY, CATEGORY_NAME VARCHAR(25),"
#                  "PARENT_ID INT(5))")
# sql = "INSERT INTO FLIPCART_CATEGORIES(CATEGORY_ID,CATEGORY_NAME,PARENT_ID) VALUES(%s,%s,%s)"
# val = [(1, 'ELECTRONICS', 0), (2, 'MOBILES', 1), (3, 'MI', 2), (4, 'VIVO', 2), (5, 'TV&APPLIANCES', 0),
#        (6, 'WASHING_MACHINE', 5)]
# mycursor.executemany(sql,val)
# db.commit()
mycursor.execute("SELECT * FROM FLIPCART_CATEGORIES WHERE PARENT_ID = 0 ")
# mycursor.execute("SELECT * FROM FLIPCART_CATEGORIES  ")

result = mycursor.fetchall()
for i in result:
    print(i)
    mycursor.execute("SELECT * FROM FLIPCART_CATEGORIES WHERE PARENT_ID = {}".format(i[0]))
    result2 = mycursor.fetchall()
    # print(result2)
    for sub in result2:
        print(sub)
        mycursor.execute("SELECT * FROM FLIPCART_CATEGORIES WHERE PARENT_ID = {}".format(sub[0]))
        result3 = mycursor.fetchall()
        # print(result2)
        for sub1 in result3:
            print(sub1)
