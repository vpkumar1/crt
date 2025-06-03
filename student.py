from db import connect
def student_menu(roll_no):
    while True:
        print
        choice =input("enter choice:")
        if choice == '1':
            view_details(roll_no)
        elif choice == '2':
            view marks(roll_no)
        elif choice == '3':
            view_timetable(roll_no)
        elif choice == '4':
            change_password(roll_no)
        



def view_details(roll):
    con=get_connect()
    cur=con.cursor()
    cur.execute("select * from students where roll_no=%s ,(roll,)")
    