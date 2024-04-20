import mysql.connector as c
mydb = c.connect(host='localhost',user='root',password='123456789',database='student')
if mydb.is_connected():
    def run(op):
        print('Your Database is [STUDENT]')
        cursor = mydb.cursor()
        if op=='1':
            select = "show tables;"
            cursor.execute(select)
            result = cursor.fetchall()
            for i in result.__iter__():
                print("Table name",i[0])
            mydb.commit()
        elif op=='2':
            select = "desc std;"
            cursor.execute(select)
            result=cursor.fetchall()
            for i in result.__iter__():
                print(f"column name = {i[0]} | datatype ={i[1]}")
            mydb.commit()
        elif op=='3':
            select = f"select * from std;"
            cursor.execute(select)
            show_database = cursor.fetchall()
            for i in show_database.__iter__():
                print(i)
        elif op=='4':
            col_name = input("Enter column name = ")
            try:
                select = f"select {col_name} from std;"
                cursor.execute(select)
                result = cursor.fetchall()
                print(f"column '{col_name}'")
                num = 1
                for i in result.__iter__():
                    print(f"{num}.",i[0])
                    num+=1
            except Exception:
                print(f"Their is no column named {col_name}")
        else:
            print("Please enter valid operation!!!")
        print('_'*80)