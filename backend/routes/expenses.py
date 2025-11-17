from flask import Blueprint, request, jsonify
from models.expense_model import add_expense, get_expenses

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/add", methods=["POST"])
def add():
    data = request.json
    add_expense(data["title"], data["amount"], data["category"])
    return jsonify({"message": "Expense Added"}), 201

@expenses_bp.route("/list", methods=["GET"])
def list_expenses():
    rows = get_expenses()
    expenses = []
    for r in rows:
        expenses.append({
            "id": r[0],
            "title": r[1],
            "amount": r[2],
            "category": r[3],
        })
    return jsonify(expenses)
from flask import Blueprint, request, jsonify
from database import get_db_connection

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/expenses", methods=["GET"])
def get_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category, date FROM expenses")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "title": row[1],
            "amount": row[2],
            "category": row[3],
            "date": row[4]
        })

    return jsonify(data)
