import mysql.connector
def connect():
    connection=mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="23hm5a0438",
        database="student_management",
    )
    return connection
if (connect()):
    print("connection established")
else:
    print("connection failed") 

