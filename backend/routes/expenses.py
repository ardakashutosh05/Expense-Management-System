from flask import Blueprint, request, jsonify
from models.expense_model import add_expense, get_expenses

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/api/expenses", methods=["GET"])
def list_expenses():
    data = get_expenses()
    return jsonify(data)

@expenses_bp.route("/api/expenses", methods=["POST"])
def create_expense():
    data = request.json
    add_expense(data["title"], data["amount"], data["category"], data["date"])
    return jsonify({"message": "Expense added"}), 201
