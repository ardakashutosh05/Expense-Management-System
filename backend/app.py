from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'database/expenses.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    amount REAL,
                    category TEXT,
                    date TEXT
                 )''')
    conn.commit()
    conn.close()

@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"id":r[0],"title":r[1],"amount":r[2],"category":r[3],"date":r[4]} for r in rows])

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    title = data.get('title')
    amount = data.get('amount')
    category = data.get('category')
    date = data.get('date') or datetime.utcnow().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
              (title, amount, category, date))
    conn.commit()
    conn.close()
    return jsonify({"message":"Expense added"}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
