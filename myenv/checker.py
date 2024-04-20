import mysql.connector as c
mydb = c.connect(host='localhost',user='root',password='123456789',database='student')
if mydb.is_connected():
    def result(sno)->None:
        cursor = mydb.cursor()
        select = f"select * from std;"
        cursor.execute(select)
        data = cursor.fetchall()
        for row in data:
            if row[1]==sno:
                return True
            