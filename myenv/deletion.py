import mysql.connector as c,checker
mydb = c.connect(host='localhost',user='root',password='123456789',database='student')
if mydb.is_connected():
    def run(op):
        cursor = mydb.cursor()   
        if op==1:
            sno = int(input("Enter serial number = "))
            if checker.result(sno)==True:
                dele = f"delete from std where sno={sno}"
                cursor.execute(dele)
                mydb.commit()
                print("DELETED!!!!!")
            else:
                    print("This Serial number is not in database")
        elif op==2:
            col_name = input("Enter column name you want to delete = ")
            try:
                dele = f"alter table std drop column {col_name};"
                cursor.execute(dele)
                mydb.commit()
            except Exception:
                print(f"Their is no column named {col_name}") 
        else:
            print("Your Database is [STUDENT] and table [STD]")
            confirm = input("You Really want to delete your table?\n->Press 'YES'")
            if confirm=='YES':
                dele=f"drop table STD;"
                cursor.execute(dele)
                mydb.commit()
                print("TABLE STD IS BEEN DELETED!!")
            else:
                print("Only 'YES' is accepted as CONFIRMATION!")


