from database import get_db_connection

def get_expenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)   # now works
    cursor.execute("SELECT id, title, amount, category, date FROM expenses")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def add_expense(title, amount, category, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (%s, %s, %s, %s)",
        (title, amount, category, date)
    )
    conn.commit()
    cursor.close()
    conn.close()
