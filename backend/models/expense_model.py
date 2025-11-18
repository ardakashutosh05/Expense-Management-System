from database import get_db_connection

# Add a new expense to the database
def add_expense(title, amount, date, category):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO expenses (title, amount, date, category) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (title, amount, date, category))
    conn.commit()
    cursor.close()
    conn.close()

# Get all expenses from the database
def get_expenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # ensures results are dicts
    cursor.execute("SELECT id, title, amount, date, category FROM expenses")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
