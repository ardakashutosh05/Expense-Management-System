from flask import Blueprint, request, jsonify
from models.expense_model import add_expense, get_expenses

# FIRST define blueprint
expenses_bp = Blueprint("expenses", __name__)

# GET expenses
@expenses_bp.route("/api/expenses", methods=["GET"])
def list_expenses():
    data = get_expenses()
    return jsonify(data)

# POST expense
@expenses_bp.route("/api/expenses", methods=["POST"])
def create_expense():
    data = request.json
    add_expense(data["title"], data["amount"], data["category"], data["date"])
    return jsonify({"message": "Expense added"}), 201
