from db import connect
conn=connect()
if conn:
     print("connection established")
else:
    print("connection failed")

roll_no=int(input("enter roll number: "))
name=input("enter name: ")
branch=input("enetr branch: ")
cursor=conn.cursor()
query="insert into student(roll_no,name,branch) values(%s,%s,%s)"
values=(roll_no,name,branch)
cursor.execute(query,values)
conn.commit()
print("Data inserted successfuly")
def fetch_data():
     cursor=conn.cursor()
     query="select * from student"
     cursor.execute(query)
     results=cursor.fetchall()
     for row in results:
          print(row)
#
def update_data():
     roll_no=int(input("enter roll number: "))
     name=input("enter name: ")
     branch=input("enter branch: ")
     cursor=conn.cursor()
     query="update student set name=%s, branch=%s ,where roll_no=%s"
     values=(name,branch,roll_no)
     cursor.execute(query,values)
     conn.commit()
     print("Data update successfully")
