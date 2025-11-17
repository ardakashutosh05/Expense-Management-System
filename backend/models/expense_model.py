import pymysql
from config import DB_CONFIG

def get_connection():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

def add_expense(title, amount, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (title, amount, category) VALUES (%s, %s, %s)",
        (title, amount, category)
    )
    conn.commit()
    conn.close()

def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows
