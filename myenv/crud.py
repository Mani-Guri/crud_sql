import mysql.connector as c,inserting as p,updating as us,read,deletion
mydb = c.connect(host='localhost',user='root',password='123456789',database='student')
if mydb.is_connected():
    print('Your Database is [STUDENT]')
    con = input("WELCOME....TO OPREATE 'CRUD' OPERATION PRESS 'yes'/'YES'/'y'/'Y' \n>>")
    while con=='YES' or con=='yes' or con=="Y" or con=='y':
        cursor = mydb.cursor()
        for num in range(1):
            select = f"select * from std"
            cursor.execute(select)
            show_database = cursor.fetchall()
            print('Your Table is [STD]')
            for i in show_database.__iter__():
                print(i)
            print('_'*80)
        operation = input("What you want to do in MySql:\n-->1.CREATE\n-->2.READ\n-->3.UPDATE\n-->4.DELETE\n>>")
        if operation=='1':
            print("inserting new records or rows into database 'STUDENT' table 'STD'")
            p.run()
        elif operation=='2':
            op = input("What you want to do?\n1.Show Tables\n2.Describe Table\n3.Show Table_Data\n4.Only column Values\n>>")
            read.run(op)
        elif operation=='3':
            op = input("What you want to update?\n1.Serial number\n2.Name\n3.Age\n4.Job_role\n5.Email\n>>")
            if op=='5':
                us.udemail()
            elif op=='4':
                us.udjob()
            elif op=='3':
                us.udage()
            elif op=='2':
                us.udname()
            elif op=='1':
                us.udsno()
            else:
                print("Enter a valid entery!!!!!")
        elif operation=='4':
            op = int(input("Which deletion want to perform?\n1.row(value)\n2.column\n3.table\n>>"))
            if op==1 or op==2 or op==3:
                deletion.run(op)
            else:
                print("Enter valid operation")
        else:
            print("Enter valid operation!!!!!")
        num = 1
        con = input("Want to Continue?? Press Yes/Y/yes/y\n>>")
else: 
    print("NOT CONNECTED TO ANY DATABASE")
print('-'*90)
print('THANK YOU!!!BYE')
