from db import connect
def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""\nAdmin menu:
          1.add students
          2.update student details
          3.reset student password
          4.update marks
          5.view all students
          6.update timetable
    """)
    def admin():
        ch=int(input("enter your choice: "))
        if ch==1:
            add_student()
        elif ch==2:
            update_student()
        elif ch==3:
            reset_student_password()
        elif ch==4:
            update_marks()
        elif ch==5:
            view_all_students()
        elif ch==6:
            update_time_table()
        elif ch==7:
            logout()
        else:
            print("invalid choice. please try again.")
    def add_student():
        conn=connnect()
        cursor=conn.cursor()
        roll_no=input("enter roll_no: ")
        name=input("enter your name: ")
        section=input("enter section")
        password=input("passwordd@123: ")
        email=input("enter email: ")
        query="insert into student(roll_no, name, class_name)"
        values=(roll_no,name,class_name,section,password,email)
        cursor.execute(query,values)
        con.commit()
        print("student added sucessfully")
    def add_student():
        pass
    def update_student():
        pass
    def reset_student_password():
        pass
    def update_marks():
        pass
    def view_all_students():
        pass
    def update_timetable():
        pass
    def logout():
        pass
    print("logging out....")
    if __name__=="__main__" ;
        