def run():
    import mysql.connector as c,datetime,random,checker
    mydb = c.connect(host='localhost',user='root',password='123456789',database='student')
    if mydb.is_connected():    
        cursor = mydb.cursor()
        num_std = int(input("Enter the number of students = "))
        i=1
        while(num_std>0):
            id = int(input(f"Enter student_id number:{i} = "))
            if checker.result(id)==None:
                name = input("Enter your name = ")
                age = int(input("Enter your age = "))
                job_role = input("Enter your Job_role = ")
                date = datetime.datetime.now()
                uid = random.randint(100,999)
                email = f"{name}@gmail.com".replace(" ","").lower()
                insert = f"insert into std values ({uid},{id},'{name}',{age},'{job_role}','{email}','{date}');"
                cursor.execute(insert)
                mydb.commit()
                num_std-=1
                i+=1
            else:
                print("With this serial number user already exist!!Please retry")
        cursor.close()
        mydb.close()

