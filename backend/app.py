from flask import Flask
from routes.expenses import expenses_bp

app = Flask(__name__)
app.register_blueprint(expenses_bp)

if __name__ == "__main__":
    print("Expense Management Backend Running!")
    app.run(debug=True, host="0.0.0.0", port=5000)
