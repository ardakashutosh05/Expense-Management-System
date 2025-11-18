from flask import Flask
from routes.expenses import expenses_bp

app = Flask(__name__)

# register blueprint
app.register_blueprint(expenses_bp)

@app.route("/")
def home():
    return "Expense Management Backend Running!"

if __name__ == "__main__":
    app.run(debug=True)
