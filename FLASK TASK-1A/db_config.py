import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vtu@26790",
        database="student_db1"
    )
